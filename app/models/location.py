import reflex as rx
import uuid
from app.constants.permissions import Permission
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING
from .relationships.location_user import LocationUser

if TYPE_CHECKING:
    from .user import User

class Location(rx.Model, table=True):
    name: str
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
    users: List["User"] = Relationship(
        back_populates="location_id",
        link_model=LocationUser,
        sa_relationship_kwargs={
            "lazy": "selectin",
            "innerjoin": True
        }
    )
