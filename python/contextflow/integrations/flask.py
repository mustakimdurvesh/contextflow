"""Flask integration for ContextFlow"""

try:
    from flask import Flask, request
except ImportError:
    raise ImportError(
        "Flask is required for this integration. "
        "Install with: pip install contextflow[flask]"
    )

from functools import wraps
from ..marker import ContextMarker
from ..scope import ContextScope


def init_contextflow(app: Flask):
    """Initialize ContextFlow integration with Flask app.
    
    Args:
        app: Flask application instance
    """
    
    @app.before_request
    def before_request():
        # Extract marker from request headers
        marker = ContextMarker.from_headers(dict(request.headers))
        
        # Set as current scope
        ContextScope.set_current(marker)
    
    @app.after_request
    def after_request(response):
        # Clear context
        ContextScope.clear_current()
        return response


def with_context(f):
    """Decorator to enable context for specific view functions.
    
    Args:
        f: View function to decorate
        
    Returns:
        Decorated function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        marker = ContextMarker.from_headers(dict(request.headers))
        with ContextScope.scope(marker):
            return f(*args, **kwargs)
    return decorated_function
