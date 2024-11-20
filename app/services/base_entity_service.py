from typing import TypeVar, Generic, Type
from app.repositories.base_repository import BaseRepository


T = TypeVar('T', bound=BaseRepository)

# A generic service class handling the business logic for classes which inherit from rx.Model
class BaseEntityService(Generic[T]):
    def __init__(self, repository: T):
        self.repository = repository