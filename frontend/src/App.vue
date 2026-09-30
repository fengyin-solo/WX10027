<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">自然保护区巡护管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向巡护路线、野生动物监测、植物资源、人为干扰、防火预警、科研监测与社区共管的一体化自然保护区巡护管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "巡护路线", path: "/patrol_route" }, { label: "巡护任务", path: "/patrol_task" }, { label: "巡护员管理", path: "/ranger" }, { label: "野生动物监测", path: "/animal" }, { label: "植物资源管理", path: "/plant" }, { label: "人为干扰监测", path: "/interference" }, { label: "栖息地管理", path: "/habitat" }, { label: "疫源疫病监测", path: "/epidemic" }, { label: "森林防火", path: "/fire_prevent" }, { label: "科研监测", path: "/research" }, { label: "社区共管", path: "/community" }, { label: "执法案件", path: "/enforcement" }, { label: "检查站管理", path: "/checkpoint" }, { label: "界碑界桩管理", path: "/boundary" }, { label: "生态修复", path: "/eco_restore" }, { label: "访客管理", path: "/visitor" }]
</script>
