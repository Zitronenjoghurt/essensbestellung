import reflex as rx
import uuid
from app.constants.permissions import Permission
from sqlalchemy import Column, UUID
from sqlmodel import Relationship, Field
from typing import List, TYPE_CHECKING
from .relationships.user_role import UserRole


class Worker(rx.Model, table=True):
    pass