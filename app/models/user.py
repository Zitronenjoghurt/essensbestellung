import reflex as rx


# Will act as an entity type but also as a model to auto-generate database migrations from.
# Since it inherits from rx.Model it already has a primary key 'id'.
class User(rx.Model, table=True):
    first_name: str
    last_name: str
    email: str
    password_hash: str