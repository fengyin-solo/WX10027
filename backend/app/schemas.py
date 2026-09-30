"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PatrolRouteEntry(BaseModel):
    """巡护路线明细结构。"""

    field_0: str | None = None  # 路线编号
    field_1: str | None = None  # 路线名称
    field_2: str | None = None  # 所属片区
    field_3: str | None = None  # 路线长度
    field_4: str | None = None  # 巡护频次
    field_5: str | None = None  # 起点坐标
    field_6: str | None = None  # 终点坐标
    field_7: str | None = None  # 路线状态

class PatrolTaskEntry(BaseModel):
    """巡护任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 巡护路线
    field_2: str | None = None  # 巡护员
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 开始时间
    field_5: str | None = None  # 结束时间
    field_6: str | None = None  # 巡护里程
    field_7: str | None = None  # 任务状态

class RangerEntry(BaseModel):
    """巡护员明细结构。"""

    field_0: str | None = None  # 巡护员编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 性别
    field_3: str | None = None  # 所属片区
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 入职日期
    field_6: str | None = None  # 从业年限
    field_7: str | None = None  # 人员状态

class AnimalEntry(BaseModel):
    """野生动物明细结构。"""

    field_0: str | None = None  # 物种名称
    field_1: str | None = None  # 保护级别
    field_2: str | None = None  # 发现地点
    field_3: str | None = None  # 发现时间
    field_4: str | None = None  # 种群数量
    field_5: str | None = None  # 栖息状况
    field_6: str | None = None  # 记录人
    field_7: str | None = None  # 记录状态

class PlantEntry(BaseModel):
    """植物资源明细结构。"""

    field_0: str | None = None  # 植物编号
    field_1: str | None = None  # 物种名称
    field_2: str | None = None  # 保护级别
    field_3: str | None = None  # 分布区域
    field_4: str | None = None  # 种群规模
    field_5: str | None = None  # 受威胁程度
    field_6: str | None = None  # 调查日期
    field_7: str | None = None  # 记录状态

class InterferenceEntry(BaseModel):
    """人为干扰事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 干扰类型
    field_2: str | None = None  # 发生地点
    field_3: str | None = None  # 发现时间
    field_4: str | None = None  # 干扰程度
    field_5: str | None = None  # 发现人
    field_6: str | None = None  # 处置措施
    field_7: str | None = None  # 事件状态

class HabitatEntry(BaseModel):
    """栖息地明细结构。"""

    field_0: str | None = None  # 栖息地编号
    field_1: str | None = None  # 栖息地名称
    field_2: str | None = None  # 栖息地类型
    field_3: str | None = None  # 面积
    field_4: str | None = None  # 主要保护对象
    field_5: str | None = None  # 退化程度
    field_6: str | None = None  # 评估日期
    field_7: str | None = None  # 管理状态

class EpidemicEntry(BaseModel):
    """疫病监测记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 监测区域
    field_2: str | None = None  # 物种名称
    field_3: str | None = None  # 样品类型
    field_4: str | None = None  # 检测项目
    field_5: str | None = None  # 检测结果
    field_6: str | None = None  # 采集日期
    field_7: str | None = None  # 记录状态

class FirePreventEntry(BaseModel):
    """防火瞭望点明细结构。"""

    field_0: str | None = None  # 瞭望点编号
    field_1: str | None = None  # 瞭望点名称
    field_2: str | None = None  # 所属片区
    field_3: str | None = None  # 海拔高程
    field_4: str | None = None  # 可视范围
    field_5: str | None = None  # 值守人员
    field_6: str | None = None  # 通讯方式
    field_7: str | None = None  # 运行状态

class ResearchEntry(BaseModel):
    """科研项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 研究领域
    field_3: str | None = None  # 合作单位
    field_4: str | None = None  # 负责人
    field_5: str | None = None  # 立项日期
    field_6: str | None = None  # 计划结题日期
    field_7: str | None = None  # 项目状态

class CommunityEntry(BaseModel):
    """社区明细结构。"""

    field_0: str | None = None  # 社区编号
    field_1: str | None = None  # 社区名称
    field_2: str | None = None  # 所属行政村
    field_3: str | None = None  # 人口数量
    field_4: str | None = None  # 主要生计来源
    field_5: str | None = None  # 共管协议日期
    field_6: str | None = None  # 联系人
    field_7: str | None = None  # 协议状态

class EnforcementEntry(BaseModel):
    """执法案件明细结构。"""

    field_0: str | None = None  # 案件编号
    field_1: str | None = None  # 案件类型
    field_2: str | None = None  # 案发地点
    field_3: str | None = None  # 案发时间
    field_4: str | None = None  # 涉案人员
    field_5: str | None = None  # 处罚决定
    field_6: str | None = None  # 承办人
    field_7: str | None = None  # 案件状态

class CheckpointEntry(BaseModel):
    """检查站明细结构。"""

    field_0: str | None = None  # 检查站编号
    field_1: str | None = None  # 检查站名称
    field_2: str | None = None  # 所在位置
    field_3: str | None = None  # 检查类型
    field_4: str | None = None  # 值守安排
    field_5: str | None = None  # 检查设备
    field_6: str | None = None  # 负责人
    field_7: str | None = None  # 运行状态

class BoundaryEntry(BaseModel):
    """界碑界桩明细结构。"""

    field_0: str | None = None  # 界桩编号
    field_1: str | None = None  # 界桩类型
    field_2: str | None = None  # 所在位置
    field_3: str | None = None  # 经纬度坐标
    field_4: str | None = None  # 设立日期
    field_5: str | None = None  # 最近核查日期
    field_6: str | None = None  # 核查人员
    field_7: str | None = None  # 界桩状态

class EcoRestoreEntry(BaseModel):
    """修复项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 修复区域
    field_3: str | None = None  # 修复类型
    field_4: str | None = None  # 承建单位
    field_5: str | None = None  # 开工日期
    field_6: str | None = None  # 计划完成日期
    field_7: str | None = None  # 项目状态

class VisitorEntry(BaseModel):
    """访客明细结构。"""

    field_0: str | None = None  # 访客编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 联系电话
    field_3: str | None = None  # 来访日期
    field_4: str | None = None  # 来访目的
    field_5: str | None = None  # 进入区域
    field_6: str | None = None  # 陪同人员
    field_7: str | None = None  # 访问状态
