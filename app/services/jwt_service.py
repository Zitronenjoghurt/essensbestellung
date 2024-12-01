import os
from datetime import timedelta, datetime
from typing import Optional

import jwt

JWT_ALGORITHM = 'HS256'
JWT_EXPIRY_MINUTES = 60 * 24 * 7
JWT_KEY = os.getenv('JWT_KEY', None)
if JWT_KEY is None:
    raise RuntimeError('JWT_KEY environment variable not set')

def jwt_encode(identifier: str, expires_delta: timedelta = None) -> str:
    to_encode = {"sub": identifier}
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=JWT_EXPIRY_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_KEY, algorithm=JWT_ALGORITHM)

def jwt_decode(jwt_token: str) -> Optional[str]:
    # ToDo: Throw different errors based on what went wrong instead of returning an Optional string
    if not isinstance(jwt_token, str):
        return None

    try:
        payload = jwt.decode(jwt_token, JWT_KEY, algorithms=[JWT_ALGORITHM])
        identifier = payload.get("sub")
    except jwt.PyJWTError:
        return None

    return identifier