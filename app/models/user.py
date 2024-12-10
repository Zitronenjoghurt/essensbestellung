import reflex as rx
import uuid
from app.constants.permissions import Permission
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING, Optional
from .relationships.user_role import UserRole
from .relationships.location_user import LocationUser

if TYPE_CHECKING:
    from .role import Role
    from .location import Location

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

    location_id: Optional[int] = Field(foreign_key="location.location_id", nullable=False)

    location: Optional["Location"] = Relationship(
        back_populates="users",
        link_model=LocationUser,
        sa_relationship_kwargs={
            "lazy": "selectin",
            "innerjoin": True
        }
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

    def get_uuid_string(self) -> str:
        return str(self.uuid)

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def add_role(self, role: "Role") -> None:
        self.roles.append(role)

    def has_permission(self, permission: Permission) -> bool:
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False