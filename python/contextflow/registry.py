"""ContextRegistry - Registry for managing context markers"""

from typing import Dict, Optional
from .marker import ContextMarker


class ContextRegistry:
    """Registry for storing and retrieving context markers.
    
    Can be used to maintain a mapping of contexts to identifiers
    for retrieving them later.
    """
    
    def __init__(self):
        """Initialize the registry."""
        self._markers: Dict[str, ContextMarker] = {}
    
    def register(self, key: str, marker: ContextMarker) -> None:
        """Register a marker with a key.
        
        Args:
            key: Unique key for the marker
            marker: The marker to register
        """
        self._markers[key] = marker
    
    def get(self, key: str) -> Optional[ContextMarker]:
        """Get a registered marker.
        
        Args:
            key: Key of the marker
            
        Returns:
            The marker or None
        """
        return self._markers.get(key)
    
    def unregister(self, key: str) -> bool:
        """Unregister a marker.
        
        Args:
            key: Key of the marker
            
        Returns:
            True if marker was unregistered, False if not found
        """
        if key in self._markers:
            del self._markers[key]
            return True
        return False
    
    def list_all(self) -> Dict[str, ContextMarker]:
        """List all registered markers.
        
        Returns:
            Copy of all registered markers
        """
        return self._markers.copy()
    
    def clear(self) -> None:
        """Clear all registered markers."""
        self._markers.clear()
    
    def __len__(self) -> int:
        """Get number of registered markers."""
        return len(self._markers)
