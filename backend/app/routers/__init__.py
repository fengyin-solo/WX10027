"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import patrol_route as router_patrol_route
from app.routers import patrol_task as router_patrol_task
from app.routers import ranger as router_ranger
from app.routers import animal as router_animal
from app.routers import plant as router_plant
from app.routers import interference as router_interference
from app.routers import habitat as router_habitat
from app.routers import epidemic as router_epidemic
from app.routers import fire_prevent as router_fire_prevent
from app.routers import research as router_research
from app.routers import community as router_community
from app.routers import enforcement as router_enforcement
from app.routers import checkpoint as router_checkpoint
from app.routers import boundary as router_boundary
from app.routers import eco_restore as router_eco_restore
from app.routers import visitor as router_visitor

ROUTERS = [router_patrol_route, router_patrol_task, router_ranger, router_animal, router_plant, router_interference, router_habitat, router_epidemic, router_fire_prevent, router_research, router_community, router_enforcement, router_checkpoint, router_boundary, router_eco_restore, router_visitor]
