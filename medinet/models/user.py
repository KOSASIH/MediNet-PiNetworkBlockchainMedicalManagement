# medinet/models/user.py

from typing import Optional

from .base_model import BaseModel

class User(BaseModel):
    """User model for MediNet"""

    username: str
    email: str
    password: str
    is_active: bool
    is_admin: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = kwargs.pop("username", "")
        self.email = kwargs.pop("email", "")
        self.password = kwargs.pop("password", "")
        self.is_active = kwargs.pop("is_active", False)
        self.is_admin = kwargs.pop("is_admin", False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active}, is_admin={self.is_admin})"

    def to_dict(self) -> Dict[str, Any]:
        """Convert the user to a dictionary"""
        user_dict = super().to_dict()
        user_dict.update({
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "is_admin": self.is_admin,
        })
        return user_dict

    def check_password(self, password: str) -> bool:
        """Check if the given password matches the user's password"""
        return self.password == password

    def set_password(self, password: str) -> None:
        """Set the user's password"""
        self.password = password

    def is_authenticated(self) -> bool:
        """Return True if the user is authenticated"""
        return True

    def is_anonymous(self) -> bool:
        """Return True if the user is anonymous"""
        return False
