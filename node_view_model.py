from marshmallow import Schema, fields, validate


class NodeSchema(Schema):
    id = fields.Str(required=True)
    parent = fields.Str(allow_none=True)


class NodesArray(Schema):
    nodes = fields.List(fields.Nested(NodeSchema), required=True, validate=validate.Length(min=1))
