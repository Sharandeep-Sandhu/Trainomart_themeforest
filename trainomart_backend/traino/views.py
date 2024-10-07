from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CourseSerializer, BlogSerializer, LeadSerializer, StudentsSerializer, ContactMessageSerializer, PaymentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Blog, Leads, Students, ContactMessage, Payment
from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from rest_framework.decorators import api_view

# Create your views here.


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['course_name']  # Allows search by course name

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Filter courses by whether they are featured"""
        featured_courses = Course.objects.filter(is_featured=True)
        serializer = self.get_serializer(featured_courses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='limited')
    def get_limited_courses(self, request):
        """Get a limited number of courses using a query parameter 'limit'"""
        limit = request.query_params.get('limit', 5)  # Default to 5 courses
        try:
            limit = int(limit)
        except ValueError:
            return Response({"error": "Invalid limit value"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Course.objects.all().order_by('-id')[:limit]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='custom-get')
    def custom_get_course_by_id(self, request, pk=None):
        """Custom action to fetch course by ID"""
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['get'], url_path='by-name')
    def get_course_by_name(self, request):
        """Get course by name"""
        course_name = request.query_params.get('name', None)
        if course_name:
            # Filtering by course name
            courses = Course.objects.filter(course_name__iexact=course_name)
            if courses.exists():
                serializer = self.get_serializer(courses, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'No course name provided'}, status=status.HTTP_400_BAD_REQUEST)

    
    
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePayment(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            user_email = serializer.validated_data['user_email']
            amount = serializer.validated_data['amount']
            currency = serializer.validated_data['currency']

            # Create a transfer quote
            quote_url = 'https://api.sandbox.transferwise.com/v1/quotes'
            quote_data = {
                "sourceCurrency": "USD",  # Replace with your source currency
                "targetCurrency": currency,
                "sourceAmount": float(amount),
                "type": "BALANCE_PAYOUT",
            }
            headers = {
                'Authorization': f'Bearer {settings.WISE_API_TOKEN}',
                'Content-Type': 'application/json',
            }
            quote_response = requests.post(quote_url, json=quote_data, headers=headers)
            if quote_response.status_code != 201:
                return Response({"error": "Failed to create quote."}, status=status.HTTP_400_BAD_REQUEST)
            quote = quote_response.json()

            # Create a transfer
            transfer_url = 'https://api.sandbox.transferwise.com/v1/transfers'
            transfer_data = {
                "targetAccount": "your_target_account_id",  # Replace with your target account ID
                "quoteUuid": quote['id'],
                "customerTransactionId": "unique_transaction_id",  # Generate unique ID
                "details": {
                    "reference": "Payment for Order #1234",
                    "transferPurpose": "verification.transfers.purpose.pay bills",  # Adjust as needed
                }
            }
            transfer_response = requests.post(transfer_url, json=transfer_data, headers=headers)
            if transfer_response.status_code != 201:
                return Response({"error": "Failed to create transfer."}, status=status.HTTP_400_BAD_REQUEST)
            transfer = transfer_response.json()

            # Fund the transfer if needed (depends on Wise API setup)
            # This step may vary based on your account setup

            # Save to database
            payment = Payment.objects.create(
                payment_id=transfer['id'],
                user_email=user_email,
                amount=amount,
                currency=currency,
                status=transfer['status'],
            )

            return Response({"payment_id": payment.payment_id, "status": payment.status}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WebhookHandler(APIView):
    def post(self, request):
        # Handle webhook data from Wise
        # Verify the webhook signature if provided
        data = request.data
        payment_id = data.get('transferUuid')
        status_update = data.get('status')

        try:
            payment = Payment.objects.get(payment_id=payment_id)
            payment.status = status_update
            payment.save()
            return Response({"message": "Payment status updated."}, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)


def index(request):
    return HttpResponse("Hello, world. You're at the trainomart index.")
