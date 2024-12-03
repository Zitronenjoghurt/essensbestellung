from datetime import timedelta

from app.services.jwt_service import jwt_encode, jwt_decode


def test_encode_decode():
    identifier = "cheesecake"
    jwt_token = jwt_encode(identifier)
    decoded_identifier = jwt_decode(jwt_token)

    assert decoded_identifier == identifier

def test_decode_failed():
    identifier = "cheesecake"
    jwt_token = jwt_encode(identifier, expires_delta=timedelta(minutes=-1))
    decoded_identifier = jwt_decode(jwt_token)

    assert decoded_identifier is None