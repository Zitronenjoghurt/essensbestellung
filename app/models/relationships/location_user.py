import reflex as rx
from sqlmodel import Field
from typing import Optional



class LocationUser(rx.Model, table=True):
    __tablename__ = "location_user"

    location_id: Optional[int] = Field(
        default=None, foreign_key="location_id", primary_key=True
    )
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )