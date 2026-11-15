"""Talk to the GitHub REST API."""
import os          # reads environment variables, like GITHUB_TOKEN (2.2)
import requests    # sends HTTP requests (Dev #4)

API = "https://api.github.com"   # every GitHub REST URL starts with this


def _headers(accept: str = "application/vnd.github+json") -> dict:
    # The _ at the start of the name means "only used inside this file". It's a habit; Python doesn't enforce it.
    # accept=...: if the caller names no format, ask for GitHub's normal JSON.
    token = os.environ.get("GITHUB_TOKEN")      # None if the variable isn't set
    if not token:                               # true for None and for an empty value
        # SystemExit: Python prints this message and stops with exit code 1, with no traceback.
        raise SystemExit("GITHUB_TOKEN is not set. Run: export GITHUB_TOKEN=$(gh auth token)")
    return {
        "Authorization": f"Bearer {token}",     # who you are (Dev #3)
        "Accept": accept,                       # which format you want back (2.6)
    }


def get_pr(repo: str, number: int) -> dict:
    """Return pull request `number` in `repo` (like "markslk/pr-buddy") as a dict."""
    r = requests.get(f"{API}/repos/{repo}/pulls/{number}", headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


def get_diff(repo: str, number: int) -> str:
    """Return the same pull request's diff as text."""
    r = requests.get(f"{API}/repos/{repo}/pulls/{number}", headers=_headers("application/vnd.github.diff"), timeout=10)
    r.raise_for_status()
    return r.text