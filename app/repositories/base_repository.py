from typing import TypeVar, Generic, Type, Optional, List
import reflex as rx
from sqlmodel import select


T = TypeVar('T', bound=rx.Model)

# A generic repository class handling basic database operations for classes which inherit from rx.Model
class BaseRepository(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    # Will overwrite if an entity of the same ID already exists in the database
    @staticmethod
    def save(entity: T) -> T:
        with rx.session() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity

    def find_one_by(self, **kwargs) -> Optional[T]:
        with rx.session() as session:
            return session.exec(
                select(self.model_class).filter_by(**kwargs)
            ).first()

    def find_all_by(self, **kwargs) -> List[T]:
        with rx.session() as session:
            entities = session.exec(
                select(self.model_class).filter_by(**kwargs)
            ).all()
            return list(entities)

    def get(self, entity_id: int) -> Optional[T]:
        return self.find_one_by(id=entity_id)