import reflex as rx
import uuid
from app.constants.permissions import Permission
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING


class Location(rx.Model, table=True):
    location_name: str
    location_id : int
    uuid: UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            unique=True,
            nullable=False,
            default=uuid.uuid4
        ),
        default_factory=uuid.uuid4
    )    