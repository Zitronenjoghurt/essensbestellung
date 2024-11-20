from enum import Enum, auto


# Since it's a string Enum, auto() will automatically add the stringified value for each enum type
# READ = auto() => READ = "READ"
# Changes to this enum will also need to be applied in a database migration
class Permission(str, Enum):
    RECEIVE_MEALS = auto()
    SERVICE_MEALS = auto()
    EDIT_ORDERS = auto()