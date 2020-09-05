from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields


class GhishOrganization(Schema):
    _id = fields.UUID(missing=uuid1)
    organization_id = fields.Integer(data_key="id")
    organization_name = fields.String(data_key="name")
    url = fields.String(data_key="html_url")
    users = fields.Nested("GhishUser", many=True, required=False, unknown=EXCLUDE)
