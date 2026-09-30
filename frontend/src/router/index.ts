import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const PatrolRoute = () => import('@/views/patrol_route/index.vue')
const PatrolTask = () => import('@/views/patrol_task/index.vue')
const Ranger = () => import('@/views/ranger/index.vue')
const Animal = () => import('@/views/animal/index.vue')
const Plant = () => import('@/views/plant/index.vue')
const Interference = () => import('@/views/interference/index.vue')
const Habitat = () => import('@/views/habitat/index.vue')
const Epidemic = () => import('@/views/epidemic/index.vue')
const FirePrevent = () => import('@/views/fire_prevent/index.vue')
const Research = () => import('@/views/research/index.vue')
const Community = () => import('@/views/community/index.vue')
const Enforcement = () => import('@/views/enforcement/index.vue')
const Checkpoint = () => import('@/views/checkpoint/index.vue')
const Boundary = () => import('@/views/boundary/index.vue')
const EcoRestore = () => import('@/views/eco_restore/index.vue')
const Visitor = () => import('@/views/visitor/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/patrol_route', name: 'patrol_route', component: PatrolRoute },
    { path: '/patrol_task', name: 'patrol_task', component: PatrolTask },
    { path: '/ranger', name: 'ranger', component: Ranger },
    { path: '/animal', name: 'animal', component: Animal },
    { path: '/plant', name: 'plant', component: Plant },
    { path: '/interference', name: 'interference', component: Interference },
    { path: '/habitat', name: 'habitat', component: Habitat },
    { path: '/epidemic', name: 'epidemic', component: Epidemic },
    { path: '/fire_prevent', name: 'fire_prevent', component: FirePrevent },
    { path: '/research', name: 'research', component: Research },
    { path: '/community', name: 'community', component: Community },
    { path: '/enforcement', name: 'enforcement', component: Enforcement },
    { path: '/checkpoint', name: 'checkpoint', component: Checkpoint },
    { path: '/boundary', name: 'boundary', component: Boundary },
    { path: '/eco_restore', name: 'eco_restore', component: EcoRestore },
    { path: '/visitor', name: 'visitor', component: Visitor },
  ],
})

export default router
