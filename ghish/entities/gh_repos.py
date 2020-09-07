from uuid import uuid1

from marshmallow import Schema, fields, EXCLUDE, pre_load


class GitHubRepoSchema(Schema):

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
    repo_id = fields.Integer()
    repo_name = fields.String()
    repo_description = fields.String()
    create_date = fields.DateTime()
    organization = fields.Nested(
            "GitHubOrganizationSchema", required=False, unknown=EXCLUDE)
    pull_requests = fields.Nested(
            "GitHubPullRequestSchema", required=False, many=True)
    url = fields.String()

    @pre_load
    def map_input_fields(self, in_data, **kwargs):
        in_data["repo_id"] = in_data.pop("id")
        in_data["repo_name"] = in_data.pop("name")
        in_data["repo_description"] = in_data.pop("description")
        in_data["create_date"] = in_data.pop("created_at")
        in_data["url"] = in_data.pop("html_url")
        return in_data
