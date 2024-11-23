import reflex as rx
from .relationships.user_role import UserRole
from app.constants.permissions import Permission
from sqlalchemy import Column, ARRAY, Enum
from sqlmodel import Field, Relationship
from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
    from .user import User

class Role(rx.Model, table=True):
    name: str
    permissions: List[Permission] = Field(
        sa_column=Column(ARRAY(Enum(Permission)), nullable=False),
    )

    # n:m Relationship between users and roles
    # Back populates the 'roles' value in the role entity
    users: List["User"] = Relationship(
        back_populates="roles",
        link_model=UserRole,
        sa_relationship_kwargs={
            "lazy": "selectin",
            "innerjoin": True
        }
    )

    def has_permission(self, permission: Permission) -> bool:
        return permission in self.permissions