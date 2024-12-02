import reflex as rx
import uuid
from app.constants.permissions import Permission
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING
from .relationships.user_role import UserRole


if TYPE_CHECKING:
    from .role import Role

# Will act as an entity type but also as a model to auto-generate database migrations from.
# Since it inherits from rx.Model it already has a primary key 'id'.
class User(rx.Model, table=True):
    first_name: str
    last_name: str
    email: str
    password_hash: str
    uuid: UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            unique=True,
            nullable=False,
            default=uuid.uuid4
        ),
        default_factory=uuid.uuid4
    )

    # n:m Relationship between users and roles
    # Back populates the 'users' value in the role entity
    roles: List["Role"] = Relationship(
        back_populates="users",
        link_model=UserRole,
        sa_relationship_kwargs={
            "lazy": "selectin",
            "innerjoin": True
        }
    )

    @property
    def uuid_string(self) -> str:
        return str(self.uuid)

    def add_role(self, role: "Role") -> None:
        self.roles.append(role)

    def has_permission(self, permission: Permission) -> bool:
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False