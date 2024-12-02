from app.services.password_service import hash_password, verify_password


def test_hash_verify():
    password = "cheesecake"
    password_hash = hash_password(password)
    assert password_hash != password
    assert verify_password(password, password_hash)
    assert not verify_password("strawberry cake", password_hash)