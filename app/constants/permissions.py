from enum import Enum, auto


# Changes to this enum will also need to be applied in a database migration
class Permission(str, Enum):
    RECEIVE_MEALS = "RECEIVE_MEALS"
    SERVICE_MEALS = "SERVICE_MEALS"
    EDIT_ORDERS = "EDIT_ORDERS"