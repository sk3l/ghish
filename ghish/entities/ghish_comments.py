from uuid import uuid1

from marshmallow import Schema, fields

from .ghish_pull_requests import GhishPullRequest
from .ghish_users import GhishUser


class GhishComment(Schema):
    _id = fields.UUID(missing=uuid1)
    comment_id = fields.Integer()
    user = fields.Nested(GhishUser)
    create_date = fields.DateTime()
    pull_request = fields.Nested(GhishPullRequest)
