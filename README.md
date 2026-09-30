# 自然保护区巡护管理平台

面向巡护路线、野生动物监测、植物资源、人为干扰、防火预警、科研监测与社区共管的一体化自然保护区巡护管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 巡护路线 | `patrol_route` | 巡护路线 | 路线编号、路线名称、所属片区 |
| 巡护任务 | `patrol_task` | 巡护任务 | 任务编号、巡护路线、巡护员 |
| 巡护员管理 | `ranger` | 巡护员 | 巡护员编号、姓名、性别 |
| 野生动物监测 | `animal` | 野生动物 | 物种名称、保护级别、发现地点 |
| 植物资源管理 | `plant` | 植物资源 | 植物编号、物种名称、保护级别 |
| 人为干扰监测 | `interference` | 人为干扰事件 | 事件编号、干扰类型、发生地点 |
| 栖息地管理 | `habitat` | 栖息地 | 栖息地编号、栖息地名称、栖息地类型 |
| 疫源疫病监测 | `epidemic` | 疫病监测记录 | 记录编号、监测区域、物种名称 |
| 森林防火 | `fire_prevent` | 防火瞭望点 | 瞭望点编号、瞭望点名称、所属片区 |
| 科研监测 | `research` | 科研项目 | 项目编号、项目名称、研究领域 |
| 社区共管 | `community` | 社区 | 社区编号、社区名称、所属行政村 |
| 执法案件 | `enforcement` | 执法案件 | 案件编号、案件类型、案发地点 |
| 检查站管理 | `checkpoint` | 检查站 | 检查站编号、检查站名称、所在位置 |
| 界碑界桩管理 | `boundary` | 界碑界桩 | 界桩编号、界桩类型、所在位置 |
| 生态修复 | `eco_restore` | 修复项目 | 项目编号、项目名称、修复区域 |
| 访客管理 | `visitor` | 访客 | 访客编号、姓名、联系电话 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
