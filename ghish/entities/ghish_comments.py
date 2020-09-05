from uuid import uuid1

from marshmallow import EXCLUDE, Schema, fields


class GhishComment(Schema):
    _id = fields.UUID(missing=uuid1)
    comment_id = fields.Integer()
    author = fields.Nested("GhishUser", required=False, unknown=EXCLUDE)
    create_date = fields.DateTime()
    pull_request = fields.Nested("GhishPullRequest", required=False, unknown=EXCLUDE)
