# medinet/models/base_model.py

from datetime import datetime
from typing import Optional

class BaseModel:
    """Base model for MediNet models"""

    id: Optional[int]
    created_at: datetime
    updated_at: datetime

    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop("id", None)
        self.created_at = kwargs.pop("created_at", datetime.now())
        self.updated_at = kwargs.pop("updated_at", datetime.now())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})"

    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def save(self) -> None:
        """Save the model to the database"""
        raise NotImplementedError

    def delete(self) -> None:
        """Delete the model from the database"""
        raise NotImplementedError
