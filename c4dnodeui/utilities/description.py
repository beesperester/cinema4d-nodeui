import c4d

def CreateCycleItems(items: list) -> c4d.BaseContainer:
    base_container = c4d.BaseContainer()

    for index, item in enumerate(items):
        base_container.SetString(index, item)

    return base_container