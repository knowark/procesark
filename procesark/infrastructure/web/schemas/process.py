from marshmallow import fields
from .entity import EntitySchema


class ProcessSchema(EntitySchema):
    name = fields.Str(example="Process name")
