import pytest
from app import User, Role
from app.constants.permissions import Permission
from app.services.password_service import hash_password
from app.state import role_repository, user_repository


@pytest.fixture(scope="session")
def test_role() -> Role:
    role = Role(name='test_role', permissions=[Permission.RECEIVE_MEALS])
    role_repository.save(role)
    yield role

@pytest.fixture(scope="session")
def test_user_password() -> str:
    return "test_password"

@pytest.fixture(scope="session")
def test_user_email() -> str:
    return "test.user@example.com"

@pytest.fixture(scope="session")
def test_user(test_role: Role, test_user_password: str, test_user_email: str) -> User:
    password_hash = hash_password(test_user_password)

    user = User(
        first_name='Test',
        last_name='User',
        email=test_user_email,
        password_hash=password_hash,
    )
    user.add_role(test_role)
    user_repository.save(user)
    yield user