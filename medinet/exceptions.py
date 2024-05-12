# medinet/exceptions.py

class MediNetError(Exception):
    """Base exception for MediNet errors"""

class ConfigError(MediNetError):
    """Error related to configuration"""

class DatabaseError(MediNetError):
    """Error related to database operations"""

class APIError(MediNetError):
    """Error related to API requests"""

class AuthenticationError(MediNetError):
    """Error related to authentication and authorization"""

class MediNetException(MediNetError):
    """Generic exception for MediNet errors"""

    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(message)

    def __repr__(self) -> str:
        return f"MediNetException(message={self.message}, code={self.code})"

    def to_dict(self) -> Dict[str, Any]:
        return {"error": self.message, "code": self.code}
