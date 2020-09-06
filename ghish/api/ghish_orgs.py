import logging

from entities.gh_organizations import GitHubOrganizationSchema

from api.ghish_http import GhishHttpAgent

LOG = logging.getLogger("ghish")


class GitHubOrgsProxy:
    def __init__(self, api_url, auth_tok):
        self._api_url = api_url
        self._auth_tok = auth_tok

    def lookup_orgs(self, org_names, include_users=False, include_repos=False):
        org_list = []
        with GhishHttpAgent(self._api_url, token=self._auth_tok) as gh_agent:
            for name in org_names:
                response = gh_agent.send_get(f"orgs/{name}")
                org = response.json()

                if include_users:
                    org["users"] = self._lookup_org_users(name)

                if include_repos:
                    org[name]["repos"] = self._lookup_org_repos(name)

            org_list.append(org)

        org_s = GitHubOrganizationSchema(many=True)
        orgs = org_s.load(org_list, partial=True)
        return orgs

    def _lookup_org_users(self, gh_agent, org_name):
        response = gh_agent.send_get(f"orgs/{org_name}/members")
        return response.json()

    def _lookup_org_repos(self, gh_agent, org_name):
        response = gh_agent.send_get(f"orgs/{org_name}/repos")
        return response.json()
