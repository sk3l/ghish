from uuid import uuid1

from marshmallow import Schema, fields

from .ghish_organizations import GhishOrganization


class GhishRepo(Schema):
    _id = fields.UUID(missing=uuid1)
    repo_name = fields.String()
    create_date = fields.DateTime()
    organization = fields.String()
    organization = fields.Nested(GhishOrganization, many=True)
    url = fields.String()
    head_commit = fields.String()
