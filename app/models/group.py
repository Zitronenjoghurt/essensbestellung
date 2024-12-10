import reflex as rx
import uuid
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING

from .relationships.worker_group import WorkerGroup

from .role import Worker


class group(rx.Model, table=True):
    work_location: int
    group_id: int
    manager: int


    members: List["Worker"] = Relationship(
        back_populates="group_id"
        link_model=WorkerGroup,
        sa_relationship_kwargs={
            "lazy": "selectin",
            "innerjoin": True
        }
    )

    def add_worker(self, worker: "Worker") -> None:
        self.worker.append(worker)

    def remove_worker(self, worker: "Worker", group_id: int) -> None:
        self.worker.remove(worker)