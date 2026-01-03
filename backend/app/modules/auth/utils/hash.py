from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(
    schemes= ["argon2"],
    deprecated = "auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()