from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields, pre_load


class GitHubComment(Schema):

    def __init__(self):
        super().__init__(unknown=EXCLUDE)

    _id = fields.UUID(missing=uuid1)
    comment_id = fields.Integer()
    author = fields.Nested("GitHubUser", required=False, unknown=EXCLUDE)
    create_date = fields.DateTime()
    pull_request = fields.Nested("GitHubPullRequest", required=False, unknown=EXCLUDE)

    @pre_load
    def map_input_fields(self, in_data, **kwargs):
        in_data["comment_id"] = in_data.pop("id")
        in_data["create_date"] = in_data.pop("created_at")
        in_data["url"] = in_data.pop("html_url")
        return in_data
