import Vue from 'vue'
import Router from 'vue-router'
import Home from "@/components/Home"
import BasicFunc from "@/components/pages/BasicFunc"
import Histogram from "@/components/pages/Histogram"
import Segmentation from "@/components/pages/Segmentation"
import Smooth from "@/components/pages/Smooth"
import Sharpen from "@/components/pages/Sharpen"
import Morphological from "@/components/pages/Morphological"
import Noise from "@/components/pages/Noise"
import Repair from "@/components/pages/Repair"

Vue.use(Router)

export default new Router({

  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/basic_func',
      name: 'BasicFunc',
      component: BasicFunc
    },
    {
      path: '/histogram',
      name: 'Histogram',
      component: Histogram
    },
    {
      path: '/segmentation',
      name: 'Segmentation',
      component: Segmentation
    }
    ,
    {
      path: '/smooth_sharpen/smooth',
      name: 'Smooth',
      component: Smooth
    }
    ,
    {
      path: '/smooth_sharpen/sharpen',
      name: 'Sharpen',
      component: Sharpen
    },
    {
      path: '/morphological',
      name: 'Morphological',
      component: Morphological
    },
    {
      path: '/fix/noise',
      name: 'Noise',
      component: Noise
    },
    {
      path: '/fix/repair',
      name: 'Repair',
      component: Repair
    }
  ]
})
