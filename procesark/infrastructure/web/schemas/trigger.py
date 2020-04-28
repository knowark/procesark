from marshmallow import fields
from .entity import EntitySchema


class TriggerSchema(EntitySchema):
    type = fields.Str(example="Trigger Type")
    pattern = fields.Str(example="CRON Pattern. e.g.: * 5 * * * ")
    process_id = fields.Str(
        data_key='processId',
        example="bc362ad7-4240-498b-a51a-44aaa09fc21f")
