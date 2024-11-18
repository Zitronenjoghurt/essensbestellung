#from typing import List
import reflex as rx
#from sqlalchemy import Column, ARRAY, Enum
#from sqlmodel import Field
#
#from app.constants.roles import Role


# Will act as an entity type but also as a
# model to auto-generate database migrations from
class User(rx.Model, table=True):
    first_name: str
    last_name: str
    email: str
    password_hash: str
    # Roles don't work yet => SQLite does not support array types => Postgresql
    # roles: List[Role] = Field(sa_column=Column(ARRAY(Enum(Role))))