from app import User, Role
from app.constants.permissions import Permission
from app.state import user_repository, role_repository


# All tests have to start with 'test_' and need to be placed in the tests directory
# They can then be run using 'make test' in the project root
def test_save_user_with_role():
    new_role = Role(name='test', permissions=[Permission.RECEIVE_MEALS])

    new_user = User(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        password_hash='thecakeisalie',
    )

    user_uuid = new_user.uuid
    new_user.add_role(new_role)
    user_repository.save(new_user)

    john_doe = user_repository.find_one_by(first_name='John', last_name='Doe')
    assert john_doe is not None
    assert john_doe.first_name == 'John'
    assert john_doe.last_name == 'Doe'
    assert john_doe.email == 'john.doe@example.com'
    assert john_doe.password_hash == 'thecakeisalie'
    assert john_doe.uuid == user_uuid
    assert john_doe.has_permission(Permission.RECEIVE_MEALS)

    test_role = role_repository.find_one_by(name='test')
    assert test_role is not None
    assert test_role.name == 'test'
    assert test_role.permissions == [Permission.RECEIVE_MEALS]