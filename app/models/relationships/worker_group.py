import reflex as rx
from sqlmodel import Field
from typing import Optional


class WorkerGroup(rx.Model, table=True):
    __tablename__ = "workers_group"

    worker_id: Optional[int] = Field(
        default=None,  foreign_key="group.id", primary_key=True
    )
    group_id: Optional[int] = Field(
        default=None, foreign_key="group_id", primary_key=True
    )
