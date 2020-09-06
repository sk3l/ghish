import logging

from entities.gh_repos import GitHubRepoSchema

from api.ghish_http import GhishHttpAgent

LOG = logging.getLogger("ghish")


class GitHubReposProxy:
    def __init__(self, api_url, auth_tok):
        self._api_url = api_url
        self._auth_tok = auth_tok

    def lookup_repos(self, repo_names, include_prs=False, include_pr_comments=False):
        repo_list = []
        with GhishHttpAgent(self._api_url, token=self._auth_tok) as gh_agent:
            for name in repo_names:
                response = gh_agent.send_get(f"repos/{name}")
                repo = response.json()

                if include_prs:
                    pull_requests = self._lookup_repo_pull_requests(name)
                    if include_pr_comments:
                        for pr in pull_requests:
                            comments = self._lookup_repo_pull_request_comments(
                                gh_agent, name, pr
                            )
                            pr["comments"] = comments
                    repo["pull_requests"] = pull_requests

            repo_list.append(repo)

        repo_s = GitHubRepoSchema(many=True)
        repos = repo_s.load(repo_list, partial=True)
        return repos

    def _lookup_repo_pull_requests(self, gh_agent, repo_name):
        response = gh_agent.send_get(f"repos/{repo_name}/pulls")
        return response.json()

    def _lookup_repo_pull_request_comments(self, gh_agent, repo_name, pr_num):
        response = gh_agent.send_get(f"repos/{repo_name}/pulls/{pr_num}/comments")
        return response.json()
