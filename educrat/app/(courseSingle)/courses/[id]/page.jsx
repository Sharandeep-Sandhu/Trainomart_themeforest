




import PageLinks from '@/components/common/PageLinks'
import Preloader from '@/components/common/Preloader'
import CourseDetailsOne from '@/components/courseSingle/CourseDetailsOne'
import CourseSlider from '@/components/courseSingle/CourseSlider'
import FooterFour from '@/components/layout/footers/FooterFour'
import FooterOne from '@/components/layout/footers/FooterOne'

import Header from '@/components/layout/headers/Header'
import HeaderFour from '@/components/layout/headers/HeaderFour'
import React from 'react'

export const metadata = {
  title: 'Couese-single-1',
  description:
    'Elevate your e-learning content with Educrat, the most impressive LMS template for online courses, education and LMS platforms.',
  
}

export default function page({ params }) {
  <Preloader/>
  return (
    <div  className="main-content  ">
        <HeaderFour/>
        <div  className="content-wrapper  js-content-wrapper ">
            <PageLinks/>
            <CourseDetailsOne id={params.id} />
            <CourseSlider/>
            <FooterFour/>
        </div>


    </div>
  )
}
