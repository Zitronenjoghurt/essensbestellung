from typing import Optional

import reflex as rx
from sqlmodel import Field


class UserRole(rx.Model, table=True):
    __tablename__ = "user_roles"

    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    role_id: Optional[int] = Field(
        default=None, foreign_key="role.id", primary_key=True
    )