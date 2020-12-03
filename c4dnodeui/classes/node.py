from c4dnodeui.types.nodetype import NodeType

class Node(
    metaclass=NodeType
):
    """
    Node
    """

    def __init__(self, data_type: id, long_id: str, **kwargs: Any) -> None:
        self.data_type = data_type
        self.long_id = long_id
        self.apply = []
        self.nodes = []
        self.dependencies = []

        if (
            "apply" in kwargs.keys() and
            isinstance(kwargs["apply"], list)
        ):
            self.apply = kwargs["apply"]

        if (
            "nodes" in kwargs.keys() and
            isinstance(kwargs["nodes"], list)
        ):
            self.nodes = kwargs["nodes"]

        if (
            "dependencies" in kwargs.keys() and
            isinstance(kwargs["dependencies"], list)
        ):
            self.dependencies = kwargs["dependencies"]

        # create data type
        self.node = c4d.GetCustomDataTypeDefault(self.data_type)

        # apply data
        for apply_callback in self.apply:
            apply_callback(self.node)
    
    def __getattr__(self, name):
        node_long_ids = [x.long_id for x in self.nodes]

        if name in node_long_ids:
            return self.nodes[node_long_ids.index(name)]
    
    @property
    def id(self) -> int:
        """
        This method implements the hashing of the long_id attribute
        as an integer
        """
        return int(
            hashlib.sha1(self.long_id.encode('utf-8')).hexdigest(), 16
        ) % (10 ** 8)
    
    @property
    def desc_id(self) -> c4d.DescID:
        return c4d.DescID(
            c4d.DescLevel(
                self.id,
                self.data_type
            )
        )

    def Register(
        self,
        group_id: c4d.DescID,
        description: c4d.Description,
        data_instance: c4d.BaseContainer
    ) -> bool:
        """
        Register node at group_id with the description base container
        """
        result = []

        resolved_dependencies = [x(data_instance) for x in self.dependencies]

        if False not in resolved_dependencies:
            result.append(
                description.SetParameter(
                    self.desc_id,
                    self.node,
                    group_id
                )
            )

        for node in self.nodes:
            result.append(
                node.Register(
                    self.desc_id,
                    description,
                    data_instance
                )
            )
        
        return False not in result
    
    def Get(
        self,
        data_instance: c4d.BaseContainer
    ) -> Any:
        return data_instance[self.id]

    def Set(
        self,
        data_instance: c4d.BaseContainer,
        value: Any
    ) -> bool:
        data_instance[self.id] = value

        return True

    def SetDefault(
        self,
        data_instance: c4d.BaseContainer,
        value: Any
    ) -> bool:
        if self.Get(data_instance) is None:
            return self.Set(data_instance, value)
        
        return True