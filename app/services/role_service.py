from app.repositories.role_repository import RoleRepository
from app.services.base_entity_service import BaseEntityService


# Will contain business logic specific to the Role entity
# This Service is class-based because it depends on stateful-operations (via the repositories) and benefits from inheritance
class RoleService(BaseEntityService[RoleRepository]):
    ...