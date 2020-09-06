from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields, pre_load


class GitHubOrganizationSchema(Schema):

    def __init__(self, many=False, unknown=EXCLUDE):
        super().__init__(many=many, unknown=unknown)

    _id = fields.UUID(missing=uuid1)
    organization_id = fields.Integer()
    organization_name = fields.String()
    url = fields.String()
    repos = fields.Nested(
            "GitHubRepoSchema", many=True, required=False, unknown=EXCLUDE)
    users = fields.Nested(
            "GitHubUserSchema", many=True, required=False, unknown=EXCLUDE)

    @pre_load
    def map_input_fields(self, in_data, **kwargs):
        in_data["organization_id"] = in_data.pop("id")
        in_data["organization_name"] = in_data.pop("login")
        in_data["url"] = in_data.pop("html_url")
        return in_data
