import reflex as rx
from sqlmodel import Field
from typing import Optional


# Table for the n:m relationship between users and roles
# Since it'll be passed as a link_model in the User and Role model, it'll automatically be created in alembic auto migrations
class UserRole(rx.Model, table=True):
    __tablename__ = "user_roles"

    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    role_id: Optional[int] = Field(
        default=None, foreign_key="role.id", primary_key=True
    )