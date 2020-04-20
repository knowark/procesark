from .entity import Entity


class Run(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.process_id = attributes['process_id']
        self.job_id = attributes['job_id']
        self.state = attributes.get('state', '')
        self.start = attributes.get('start', 0)
        self.end = attributes.get('end', 0)
