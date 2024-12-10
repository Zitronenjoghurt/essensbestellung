import reflex as rx
import uuid
from app.constants.permissions import Permission
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING, Optional

from .user import User
from .relationships.worker_group import WorkerGroup
from .group import Group


class Worker (User, table=True):
    group_id: int = Field(foreign_key="group.group_id", nullable=False)
    
    group: Optional[Group] = Relationship(
        back_populates="members",
        link_model=WorkerGroup,
        sa_relationship_kwargs={
            "lazy": "selectin",
            "innerjoin": True
        }
    )
    
    #qr_code: 
