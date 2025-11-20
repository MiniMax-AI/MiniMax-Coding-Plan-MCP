"""Custom exceptions for Minimax MCP."""

class MinimaxAPIError(Exception):
    """Base exception for Minimax API errors."""
    pass

class MinimaxAuthError(MinimaxAPIError):
    """Authentication related errors."""
    pass

class MinimaxRequestError(MinimaxAPIError):
    """Request related errors."""
    pass

class MinimaxTimeoutError(MinimaxAPIError):
    """Timeout related errors."""
    pass

class MinimaxValidationError(MinimaxAPIError):
    """Validation related errors."""
    pass 

class MinimaxMcpError(MinimaxAPIError):
    pass
