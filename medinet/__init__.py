# medinet/__init__.py

from importlib import metadata

__version__ = metadata.version("medinet")

from .config import Config
from .exceptions import MediNetError

__all__ = ["Config", "MediNetError"]
