import logging

from entities.gh_pull_requests import GitHubPullRequestSchema

from api.ghish_http import GhishHttpAgent

LOG = logging.getLogger("ghish")


class GitHubPullRequestsProxy:
    def __init__(self, api_url, auth_tok):
        self._api_url = api_url
        self._auth_tok = auth_tok

    def lookup_pull_requests(self, repo_name, pr_nums, include_pr_comments=False):
        pr_list = []
        with GhishHttpAgent(self._api_url, token=self._auth_tok) as gh_agent:
            for pr in pr_nums:
                results = gh_agent.send_get(f"repos/{repo_name}/pulls/{pr}")

                pull_request = results.data()[0]
                if include_pr_comments:
                    comments = self._lookup_repo_pull_request_comments(
                        gh_agent, repo_name, pr
                    )
                    pull_request["pr_comments"] = comments

                pr_list.append(pull_request)

        pull_request_s = GitHubPullRequestSchema(many=True)
        pull_requests = pull_request_s.load(pr_list, partial=True)
        return pull_requests

    def _lookup_repo_pull_request_comments(self, gh_agent, repo_name, pr_num):
        results = gh_agent.send_get(f"repos/{repo_name}/pulls/{pr_num}/comments")
        return results.data()
