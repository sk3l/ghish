from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields


class GhishPullRequest(Schema):
    _id = fields.UUID(missing=uuid1)
    pr_id = fields.Integer(data_key="id")
    repo = fields.Nested("GhishRepo", required=False, unknown=EXCLUDE)
    title = fields.String()
    author = fields.Nested(
        "GhishUser", data_key="user", required=False, unknown=EXCLUDE
    )
    create_date = fields.DateTime(data_key="created_at")
    url = fields.String(data_key="html_url")
    comment_count = fields.Integer(data_key="comments")
    review_comment_count = fields.Integer(data_key="review_comments")
    pr_comments = fields.Nested(
        "GhishComment", many=True, required=False, unknown=EXCLUDE
    )
