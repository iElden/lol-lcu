class LoLLCUException(Exception):
    """Base exception"""

class HTTPException(LoLLCUException):
    """Exception raised when http request fail"""