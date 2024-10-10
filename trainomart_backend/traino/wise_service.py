# wise_service.py

import requests
from django.conf import settings

WISE_API_BASE_URL = "https://api.transferwise.com/v1"

def get_headers():
    return {
        "Authorization": f"Bearer {settings.WISE_API_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

def create_quote(source_currency, target_currency, source_amount):
    url = f"{WISE_API_BASE_URL}/quotes"
    payload = {
        "sourceCurrency": source_currency,
        "targetCurrency": target_currency,
        "sourceAmount": source_amount,
    }
    response = requests.post(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.json()

def create_transfer(profile_id, quote_id, target_account_id, customer_transaction_id):
    url = f"{WISE_API_BASE_URL}/transfers"
    payload = {
        "targetAccount": target_account_id,
        "quote": quote_id,
        "customerTransactionId": customer_transaction_id,
    }
    response = requests.post(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.json()

# Add more functions as needed (e.g., get_transfer_status, list_accounts)
