from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields, pre_load


class GitHubCommentSchema(Schema):

    def __init__(self,
                 many=False,
                 unknown=EXCLUDE,
                 only=None,
                 exclude=(),
                 context=None,
                 load_only=(),
                 dump_only=(),
                 partial=False):
        super().__init__(many=many,
                         unknown=unknown,
                         only=only,
                         exclude=exclude,
                         context=context,
                         load_only=load_only,
                         dump_only=dump_only,
                         partial=partial)

    _id = fields.UUID(missing=uuid1)
    comment_id = fields.Integer()
    author = fields.Nested("GitHubUserSchema", required=False, unknown=EXCLUDE)
    create_date = fields.DateTime()
    pull_request = fields.Nested("GitHubPullRequestSchema", required=False, unknown=EXCLUDE)

    @pre_load
    def map_input_fields(self, in_data, **kwargs):
        in_data["comment_id"] = in_data.pop("id")
        in_data["create_date"] = in_data.pop("created_at")
        in_data["url"] = in_data.pop("html_url")
        return in_data
