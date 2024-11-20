from app import User
from app.repositories.base_repository import BaseRepository


# Will contain database operations specific to the User entity
class UserRepository(BaseRepository[User]):
    ...