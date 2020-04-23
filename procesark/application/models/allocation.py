from .entity import Entity


class Allocation(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.process_id = attributes['process_id']
        self.job_id = attributes['job_id']
        self.sequence = attributes.get('sequence', 1)
