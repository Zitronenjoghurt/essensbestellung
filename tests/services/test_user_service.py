import pytest
from app import User
from app.errors.authentication_errors import InvalidCredentialsError
from app.services.jwt_service import jwt_decode
from app.state import user_service
from uuid import UUID


def test_session_token_generation(test_user: User, test_user_email: str, test_user_password: str):
    with pytest.raises(InvalidCredentialsError):
        user_service.generate_session_token("super_wrong_email", test_user_password)

    with pytest.raises(InvalidCredentialsError):
        user_service.generate_session_token(test_user_email, "super_wrong_password")

    token = user_service.generate_session_token(test_user_email, test_user_password)
    assert isinstance(token, str)

    uuid_string = jwt_decode(token)
    assert isinstance(uuid_string, str)

    try:
        uuid = UUID(uuid_string)
    except ValueError:
        uuid = None
    assert isinstance(uuid, UUID)

    assert test_user.uuid == uuid