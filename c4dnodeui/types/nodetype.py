import c4d
import c4dnodeui

from typing import Callable, Any

class NodeType(type):

    def __getattr__(cls, name):
        if name.startswith("Set"):
            def callback(
                desc_id: c4d.DescID,
                value: Any
            ) -> Callable:
                def apply_callback(node) -> Callable:
                    getattr(node, name)(desc_id, value)
                
                return apply_callback

            return callback
    
    def CompareEqual(
        cls,
        node,
        value: Any
    ) -> Callable:
        def callback(data_instance: c4d.BaseContainer) -> bool:
            return (node.Get(data_instance) == value)
        
        return callback
    
    def CompareGreater(
        cls,
        node,
        value: Any
    ) -> Callable:
        def callback(data_instance: c4d.BaseContainer) -> bool:
            return (node.Get(data_instance) > value)
        
        return callback
    
    def CompareGreaterOrEqual(
        cls,
        node,
        value: Any
    ) -> Callable:
        def callback(data_instance: c4d.BaseContainer) -> bool:
            return (node.Get(data_instance) >= value)
        
        return callback
    
    def CompareSmaller(
        cls,
        node,
        value: Any
    ) -> Callable:
        def callback(data_instance: c4d.BaseContainer) -> bool:
            return (node.Get(data_instance) < value)
        
        return callback
    
    def CompareSmallerOrEqual(
        cls,
        node,
        value: Any
    ) -> Callable:
        def callback(data_instance: c4d.BaseContainer) -> bool:
            return (node.Get(data_instance) <= value)
        
        return callback