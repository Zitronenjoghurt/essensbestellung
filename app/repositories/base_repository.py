from typing import TypeVar, Generic, Type, Optional, List, Any
import reflex as rx
from sqlmodel import select


T = TypeVar('T', bound=rx.Model)

# A generic repository class handling basic database operations for classes which inherit from rx.Model
class BaseRepository(Generic[T]):

    # Will overwrite if an entity of the same ID already exists in the database
    @staticmethod
    def save(entity: T) -> T:
        with rx.session() as session:
            session.add(entity)
            session.commit()
            return entity

    @staticmethod
    def find_one_by(**kwargs) -> Optional[T]:
        with rx.session() as session:
            return session.exec(
                select(T).filter_by(**kwargs)
            ).first()

    @staticmethod
    def find_all_by(**kwargs) -> List[T]:
        with rx.session() as session:
            entities = session.exec(
                select(T).filter_by(**kwargs)
            ).all()
            return list(entities)

    def get(self, entity_id: int) -> Optional[T]:
        return self.find_one_by(id=entity_id)