class NodeType(type):

    def __getattr__(cls, name):
        if name.startswith("Set"):
            def callback(desc_id, value):
                def apply_callback(node):
                    getattr(node, name)(desc_id, value)
                
                return apply_callback

            return callback
    
    def CompareEqual(cls, node, value):
        def callback(data_instance):
            return (node.Get(data_instance) == value)
        
        return callback
    
    def CompareGreater(cls, node, value):
        def callback(data_instance):
            return (node.Get(data_instance) > value)
        
        return callback
    
    def CompareGreaterOrEqual(cls, node, value):
        def callback(data_instance):
            return (node.Get(data_instance) >= value)
        
        return callback
    
    def CompareSmaller(cls, node, value):
        def callback(data_instance):
            return (node.Get(data_instance) < value)
        
        return callback
    
    def CompareSmallerOrEqual(cls, node, value):
        def callback(data_instance):
            return (node.Get(data_instance) <= value)
        
        return callback