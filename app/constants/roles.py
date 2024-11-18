from enum import Enum


# Just an idea for how we could handle the different kinds of permissions
# Adding these to a user entity and if they try to access certain routes we will check if they have permissions to do so, etc.
class Role(str, Enum):
    EMPLOYEE = "employee"                   # Mitarbeiter
    KITCHEN_PERSONELL = "kitchen_personell" # Küchenpersonal