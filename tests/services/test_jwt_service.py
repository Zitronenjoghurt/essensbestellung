import pytest
from app.errors.authentication_errors import ExpiredSessionTokenError
from app.services.jwt_service import jwt_encode, jwt_decode
from datetime import timedelta


def test_encode_decode():
    identifier = "cheesecake"
    jwt_token = jwt_encode(identifier)
    decoded_identifier = jwt_decode(jwt_token)

    assert decoded_identifier == identifier

def test_decode_failed():
    with pytest.raises(ExpiredSessionTokenError):
        identifier = "cheesecake"
        jwt_token = jwt_encode(identifier, expires_delta=timedelta(minutes=-1))
        jwt_decode(jwt_token)