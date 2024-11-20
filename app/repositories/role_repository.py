from app import Role
from app.repositories.base_repository import BaseRepository


# Will contain database operations specific to the User entity
class RoleRepository(BaseRepository[Role]):
    def __init__(self):
        super().__init__(Role)