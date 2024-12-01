from typing import Optional
from uuid import UUID

from app import User
from app.repositories.base_repository import BaseRepository


# Will contain database operations specific to the User entity
class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def find_by_uuid(self, uuid: UUID) -> Optional[User]:
        return self.find_one_by(uuid=uuid)