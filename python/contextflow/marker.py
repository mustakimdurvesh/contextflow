"""ContextMarker - Core context propagation mechanism"""

import uuid
from typing import Any, Dict, Optional
from datetime import datetime
import msgpack
import base64


class ContextMarker:
    """A marker for propagating context across boundaries.
    
    ContextMarker acts as a container for metadata that needs to be
    propagated across service boundaries, async operations, and execution
    contexts.
    
    Attributes:
        marker_id: Unique identifier for this marker
        data: Dictionary containing context data
        created_at: Timestamp when marker was created
    """
    
    HEADER_PREFIX = 'X-Context-Flow-'
    MARKER_HEADER = 'X-Context-Flow-Marker'
    
    def __init__(self, marker_id: Optional[str] = None):
        """Initialize a ContextMarker.
        
        Args:
            marker_id: Optional unique identifier. Generated if not provided.
        """
        self.marker_id = marker_id or str(uuid.uuid4())
        self.data: Dict[str, Any] = {}
        self.created_at = datetime.utcnow().isoformat()
    
    def set(self, key: str, value: Any) -> 'ContextMarker':
        """Set a value in the context.
        
        Args:
            key: The context key
            value: The value to set
            
        Returns:
            Self for method chaining
        """
        if not isinstance(key, str):
            raise TypeError(f"Key must be string, got {type(key)}")
        self.data[key] = value
        return self
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the context.
        
        Args:
            key: The context key
            default: Default value if key not found
            
        Returns:
            The value or default
        """
        return self.data.get(key, default)
    
    def has(self, key: str) -> bool:
        """Check if a key exists in the context.
        
        Args:
            key: The context key
            
        Returns:
            True if key exists, False otherwise
        """
        return key in self.data
    
    def delete(self, key: str) -> bool:
        """Delete a value from the context.
        
        Args:
            key: The context key
            
        Returns:
            True if deleted, False if not found
        """
        if key in self.data:
            del self.data[key]
            return True
        return False
    
    def to_dict(self) -> Dict[str, Any]:
        """Export marker as dictionary.
        
        Returns:
            Dictionary representation of marker
        """
        return {
            'marker_id': self.marker_id,
            'data': self.data,
            'created_at': self.created_at,
        }
    
    def to_headers(self) -> Dict[str, str]:
        """Export marker as HTTP headers.
        
        Returns:
            Dictionary of HTTP headers
        """
        headers = {}
        headers[self.MARKER_HEADER] = self.marker_id
        
        # Encode the data as msgpack and base64 for transport
        encoded = msgpack.packb(self.data)
        encoded_b64 = base64.b64encode(encoded).decode('utf-8')
        headers[f'{self.HEADER_PREFIX}Data'] = encoded_b64
        headers[f'{self.HEADER_PREFIX}CreatedAt'] = self.created_at
        
        return headers
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ContextMarker':
        """Create marker from dictionary.
        
        Args:
            data: Dictionary with marker data
            
        Returns:
            ContextMarker instance
        """
        marker = cls(marker_id=data.get('marker_id'))
        marker.data = data.get('data', {})
        return marker
    
    @classmethod
    def from_headers(cls, headers: Dict[str, str]) -> 'ContextMarker':
        """Create marker from HTTP headers.
        
        Args:
            headers: HTTP headers dictionary
            
        Returns:
            ContextMarker instance
        """
        # Case-insensitive header lookup
        headers_lower = {k.lower(): v for k, v in headers.items()}
        
        marker_id = headers_lower.get(cls.MARKER_HEADER.lower())
        if not marker_id:
            # Create new marker if not found
            return cls()
        
        marker = cls(marker_id=marker_id)
        
        # Decode data
        data_b64 = headers_lower.get(f'{cls.HEADER_PREFIX}Data'.lower())
        if data_b64:
            try:
                encoded = base64.b64decode(data_b64)
                marker.data = msgpack.unpackb(encoded, raw=False)
            except Exception as e:
                print(f"Warning: Could not decode marker data: {e}")
        
        created_at = headers_lower.get(f'{cls.HEADER_PREFIX}CreatedAt'.lower())
        if created_at:
            marker.created_at = created_at
        
        return marker
    
    def __repr__(self) -> str:
        """String representation of marker."""
        return f"ContextMarker(id={self.marker_id}, keys={list(self.data.keys())})"
