import c4d


def Render(ui_root, ui_nodes):
    def GetDDescription(self, node, description, flags):
        data_instance = node.GetDataInstance()

        if data_instance is None:
            return False

        # Load the description
        if not description.LoadDescription(node.GetType()):
            return False 

        # adds all nodeui instances to ui_root layout
        single_id = description.GetSingleDescID()
        root_id = c4d.DescID(ui_root)

        for ui_node in ui_nodes:
            ui_node.Register(root_id, description, data_instance, single_id)

        return (True, flags | c4d.DESCFLAGS_DESC_LOADED)
    
    return GetDDescription
