from uuid import uuid1

from marshmallow import Schema, fields

from .ghish_organizations import GhishOrganization


class GhishUser(Schema):
    _id = fields.UUID(missing=uuid1)
    user_name = fields.String()
    email = fields.String()
    organization = fields.Nested(GhishOrganization, many=True)
    url = fields.String()
