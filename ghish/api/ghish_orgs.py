import logging

from entities.gh_organizations import GitHubOrganization

from api.ghish_http import GhishHttpAgent

LOG = logging.getLogger("ghish")


class GhishOrgsProxy:
    def __init__(self, api_url, auth_tok):
        self._api_url = api_url
        self._auth_tok = auth_tok

    def lookup_orgs(self, org_names):
        orgs = GitHubOrganization()
        with GhishHttpAgent(self._api_url) as gh_agent:
            vars(gh_agent)

        return orgs
