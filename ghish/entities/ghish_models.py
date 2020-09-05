from uuid import uuid1

from marshmallow import Schema, fields


class GhishOrganization(Schema):
    _id = fields.UUID(missing=uuid1)
    organization_name = fields.String()
    url = fields.String()
