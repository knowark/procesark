from .entity import Entity


class Job(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.name = attributes.get('name', '')
        self.context = attributes.get('context', {})
