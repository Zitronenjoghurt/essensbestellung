import reflex as rx
from app.constants.permissions import Permission
from sqlmodel import Relationship
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

    def add_role(self, role: "Role") -> None:
        self.roles.append(role)

    def has_permission(self, permission: Permission) -> bool:
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False