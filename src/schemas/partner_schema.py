from marshmallow import Schema, fields

class PartnerDeserializeSchema(Schema):
    partner = fields.String(required=True)

class PartnerSerializeSchema(Schema):
    id = fields.UUID()
    partner = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')