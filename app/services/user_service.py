from app.repositories.user_repository import UserRepository
from app.services.base_entity_service import BaseEntityService


# Will contain business logic specific to the User entity
# This Service is class-based because it depends on stateful-operations (via the repositories) and benefits from inheritance
class UserService(BaseEntityService[UserRepository]):
    ...