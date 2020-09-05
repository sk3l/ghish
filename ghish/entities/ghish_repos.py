from uuid import uuid1

from marshmallow import Schema, fields, EXCLUDE


class GhishRepo(Schema):

    _id = fields.UUID(missing=uuid1)
    repo_id = fields.Integer(data_key='id')
    repo_name = fields.String(data_key='name')
    repo_description = fields.String(data_key='description')
    create_date = fields.DateTime(data_key='created_at')
    organization = fields.Nested("GhishOrganization", required=False, unknown=EXCLUDE)
    url = fields.String(data_key='html_url')
