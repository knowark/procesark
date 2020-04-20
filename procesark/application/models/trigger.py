from .entity import Entity


class Trigger(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.type = attributes.get('type', 'direct')
        self.process_id = attributes['process_id']
