from uuid import uuid1

from marshmallow import Schema, EXCLUDE, fields


class GhishUser(Schema):
    _id = fields.UUID(missing=uuid1)
    user_id = fields.Integer(data_key="id")
    user_name = fields.String(data_key="login")
    email = fields.Email()
    organizations = fields.Nested("GhishOrganization", many=True, required=False, unknown=EXCLUDE)
    url = fields.String(data_key="html_url")
