




import About from '@/components/about/About'


import Brands from '@/components/common/Brands'
import Instructors from '@/components/common/Instructors'
import PageLinks from '@/components/common/PageLinks'
import Preloader from '@/components/common/Preloader'
import TestimonialsOne from '@/components/common/TestimonialsOne'
import WhyCourse from '@/components/homes/WhyCourse'
import FooterFour from '@/components/layout/footers/FooterFour'


import FooterOne from '@/components/layout/footers/FooterOne'
import Header from '@/components/layout/headers/Header'
import HeaderFour from '@/components/layout/headers/HeaderFour'
import React from 'react'

export const metadata = {
  title: 'about',
  description:
    '',
  
}

export default function page() {
  return (
    <div className="main-content  ">
      <Preloader/>

        <HeaderFour/>
        <div className="content-wrapper js-content-wrapper overflow-hidden">
            <PageLinks/>
            <About/>
            <WhyCourse/>
            

            <TestimonialsOne/>
            <Instructors/>
            <Brands/>
           

            
            
            <FooterFour/>
        </div>

    </div>
  )
}

