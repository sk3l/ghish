from uuid import uuid1

from marshmallow import Schema, fields

from .ghish_comments import GhishComment
from .ghish_repos import GhishRepo
from .ghish_users import GhishUser


class GhishPullRequest(Schema):
    _id = fields.UUID(missing=uuid1)
    title = fields.String()
    repo = fields.Nested(GhishRepo)
    author = fields.Nested(GhishUser)
    create_date = fields.DateTime()
    status = fields.String()
    url = fields.String()
    comments = fields.Nested(GhishComment, many=True)
