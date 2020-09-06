import argparse
import sys


def _parse_args():
    parser = argparse.ArgumentParser(
        prog="ghish", description="GitHub Metadata Lookup Tool"
    )
    cmd_parsers = parser.add_subparsers(
        title="lookup modes",
        description="Lookup GitHub metadata by one of the following dimensions",
    )

    orgs_parser = cmd_parsers.add_parser("orgs", help="Lookup info on organizations")
    orgs_parser.add_argument(
        "-u",
        "--users",
        action="store_true",
        help="Include users belonging to the organization",
    )
    orgs_parser.add_argument(
        "-r",
        "--repos",
        action="store_true",
        help="Include repos in the organization",
    )
    orgs_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Lookup argument is a comma-delimited list of names",
    )
    orgs_parser.add_argument("org_name", help="Organization name to lookup")

    users_parser = cmd_parsers.add_parser("users", help="Lookup info on users")
    users_parser.add_argument(
        "-o",
        "--orgs",
        action="store_true",
        help="Include organizations the user belongs to",
    )
    users_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Lookup argument is a comma-delimited list of names",
    )
    users_parser.add_argument("user_name", help="User name to lookup")

    repos_parser = cmd_parsers.add_parser("repos", help="Lookup info on repositories")
    repos_parser.add_argument(
        "-p",
        "--pull-requests",
        choices=["open", "closed", "merged", "all"],
        help="Include repo pull requests with given status",
    )
    repos_parser.add_argument(
        "-c",
        "--comments",
        action="store_true",
        help="Include pull request comments (requires --pull-requests)",
    )
    repos_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Lookup argument is a comma-delimited list of names",
    )
    repos_parser.add_argument(
        "repo_name", help="Fully-qualified repo name (ORG/REPO) to lookup"
    )

    prs_parser = cmd_parsers.add_parser(
        "pull_requests", help="Lookup info on pull requests"
    )
    prs_parser.add_argument(
        "-c",
        "--comments",
        action="store_true",
        help="Include pull request comments",
    )
    prs_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Lookup argument is a comma-delimited list of pull requests",
    )
    prs_parser.add_argument(
        "pr_num", help="Fully-qualified pull requests (ORG/REPO/PRNUM) to lookup"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()
    parser.parse_args()


if __name__ == "__main__":
    _parse_args()
