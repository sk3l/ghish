from uuid import uuid1

from marshmallow import Schema, EXCLUDE, fields, pre_load


class GitHubUserSchema(Schema):

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
    user_id = fields.Integer()
    user_name = fields.String()
    email = fields.Email()
    organizations = fields.Nested(
            "GitHubOrganizationSchema", many=True, required=False, unknown=EXCLUDE)
    url = fields.String()

    @pre_load
    def map_input_fields(self, in_data, **kwargs):
        in_data["user_id"] = in_data.pop("id")
        in_data["user_name"] = in_data.pop("login")
        in_data["url"] = in_data.pop("html_url")
        return in_data
