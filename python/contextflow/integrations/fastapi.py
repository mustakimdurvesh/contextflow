"""FastAPI integration for ContextFlow"""

try:
    from fastapi import Request
    from fastapi.middleware.base import BaseHTTPMiddleware
except ImportError:
    raise ImportError(
        "FastAPI is required for this integration. "
        "Install with: pip install contextflow[fastapi]"
    )

from ..marker import ContextMarker
from ..scope import ContextScope


class ContextFlowMiddleware(BaseHTTPMiddleware):
    """FastAPI middleware for automatic context propagation.
    
    This middleware automatically:
    - Extracts context from incoming request headers
    - Sets it as the current scope
    - Propagates it to outgoing responses
    """
    
    async def dispatch(self, request: Request, call_next):
        # Extract marker from request headers
        marker = ContextMarker.from_headers(dict(request.headers))
        
        # Set as current context
        with ContextScope.scope(marker):
            # Process the request
            response = await call_next(request)
        
        # Add context headers to response
        for key, value in marker.to_headers().items():
            response.headers[key] = value
        
        return response
