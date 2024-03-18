from passlib.context import CryptContext


def get_password_hash(password):
    bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return bcrypt_context.hash(password)