from .entity import Entity


class Process(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.name = attributes.get('name', '')
        self.context = attributes.get('context', {})
