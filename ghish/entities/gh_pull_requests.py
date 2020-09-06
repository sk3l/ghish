from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields, pre_load


class GitHubPullRequestSchema(Schema):

    def __init__(self):
        super().__init__(unknown=EXCLUDE)

    _id = fields.UUID(missing=uuid1)
    pr_id = fields.Integer()
    repo = fields.Nested("GitHubRepoSchema", required=False, unknown=EXCLUDE)
    title = fields.String()
    author = fields.Nested("GitHubUserSchema", required=False, unknown=EXCLUDE)
    create_date = fields.DateTime()
    comment_count = fields.Integer()
    review_comment_count = fields.Integer()
    pr_comments = fields.Nested(
        "GitHubCommentSchema", many=True, required=False, unknown=EXCLUDE
    )
    url = fields.String()

    @pre_load
    def map_input_fields(self, in_data, **kwargs):
        in_data["pr_id"] = in_data.pop("id")
        in_data["author"] = in_data.pop("user")
        in_data["create_date"] = in_data.pop("created_at")
        in_data["comment_count"] = in_data.pop("comments")
        in_data["review_comment_count"] = in_data.pop("review_comments")
        in_data["url"] = in_data.pop("html_url")
        return in_data
