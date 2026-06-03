"""ContextScope - Scope management for context lifecycle"""

from typing import Optional
from contextlib import contextmanager
import contextvars

from .marker import ContextMarker


class ContextScope:
    """Manages the lifecycle and scope of a ContextMarker.
    
    ContextScope provides utilities for working with context markers
    within specific scopes (e.g., request scope, task scope).
    """
    
    _current_marker: contextvars.ContextVar[Optional[ContextMarker]] = contextvars.ContextVar(
        'current_marker', default=None
    )
    
    @classmethod
    def set_current(cls, marker: ContextMarker) -> None:
        """Set the current context marker.
        
        Args:
            marker: The marker to set as current
        """
        cls._current_marker.set(marker)
    
    @classmethod
    def get_current(cls) -> Optional[ContextMarker]:
        """Get the current context marker.
        
        Returns:
            The current marker or None
        """
        return cls._current_marker.get()
    
    @classmethod
    def clear_current(cls) -> None:
        """Clear the current context marker."""
        cls._current_marker.set(None)
    
    @classmethod
    @contextmanager
    def scope(cls, marker: Optional[ContextMarker] = None):
        """Context manager for scope management.
        
        Args:
            marker: Marker to use for this scope. Creates new if not provided.
            
        Yields:
            The marker for this scope
        """
        if marker is None:
            marker = ContextMarker()
        
        previous = cls.get_current()
        cls.set_current(marker)
        
        try:
            yield marker
        finally:
            cls.set_current(previous)
    
    @classmethod
    @contextmanager
    def child_scope(cls, **kwargs):
        """Create a child scope inheriting from current marker.
        
        Args:
            **kwargs: Initial values for child scope
            
        Yields:
            The new child marker
        """
        parent = cls.get_current()
        child = ContextMarker()
        
        # Inherit parent data if exists
        if parent:
            child.data = parent.data.copy()
        
        # Add/override with kwargs
        for key, value in kwargs.items():
            child.set(key, value)
        
        with cls.scope(child):
            yield child
