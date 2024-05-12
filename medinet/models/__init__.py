# medinet/models/__init__.py

from importlib import metadata

__version__ = metadata.version("medinet")

from .base_model import BaseModel
from .user import User

__all__ = ["BaseModel", "User"]
