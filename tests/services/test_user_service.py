from uuid import UUID

from app import User
from app.services.jwt_service import jwt_decode
from app.state import user_service


def test_session_token_generation(test_user: User, test_user_email: str, test_user_password: str):
    wrong_email = user_service.generate_session_token("super_wrong_email", test_user_password)
    assert wrong_email is None

    wrong_password = user_service.generate_session_token(test_user_email, "super_wrong_password")
    assert wrong_password is None

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