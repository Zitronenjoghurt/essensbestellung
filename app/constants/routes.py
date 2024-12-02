from enum import Enum


# To prevent mix-ups and ensure routing consistency
class Route(str, Enum):
    ROOT = "/"
    EXAMPLE = "/example"
    LOGIN = "/login"
