from .entity import Entity


class Trigger(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.type = attributes.get('type', 'cron')
        self.pattern = attributes.get('pattern', '* * * * *')
        self.process_id = attributes['process_id']
