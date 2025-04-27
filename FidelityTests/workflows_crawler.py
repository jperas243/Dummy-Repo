import requests
from urllib.parse import quote
import time

# === CONFIG ===
GITHUB_TOKEN = "your_token_here"  # Add your GitHub personal access token here
LANGUAGE = "Python"
MIN_STARS = 100
MIN_WORKFLOW_COMMITS = 3
MAX_REPOS = 50  # How many repositories to check (you can raise this)

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def search_repositories(language, min_stars, max_repos):
    repos = []
    page = 1
    while len(repos) < max_repos:
        query = f"language:{language} stars:>={min_stars}"
        url = f"https://api.github.com/search/repositories?q={quote(query)}&sort=stars&order=desc&per_page=30&page={page}"
        print(f"Searching: {url}")
        resp = requests.get(url, headers=HEADERS)
        data = resp.json()
        items = data.get("items", [])
        if not items:
            break
        repos.extend(items)
        if len(items) < 30:
            break
        page += 1
        time.sleep(1)  # avoid rate limiting
    return repos[:max_repos]

def has_workflows(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/contents/.github/workflows"
    resp = requests.get(url, headers=HEADERS)
    return resp.status_code == 200 and isinstance(resp.json(), list)

def count_workflow_commits(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/commits"
    params = {"path": ".github/workflows", "per_page": 100}
    commits = []
    page = 1
    while True:
        params["page"] = page
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code != 200:
            break
        batch = resp.json()
        if not batch:
            break
        commits.extend(batch)
        page += 1
        time.sleep(0.5)
    return len(commits)

def main():
    print(f"Searching for {LANGUAGE} repos with >= {MIN_STARS} stars...")
    repos = search_repositories(LANGUAGE, MIN_STARS, MAX_REPOS)
    print(f"Found {len(repos)} repositories.")

    for repo in repos:
        full_name = repo["full_name"]
        html_url = repo["html_url"]
        print(f"\nChecking {full_name}...")

        if not has_workflows(full_name):
            print(" - No workflows found.")
            continue

        commit_count = count_workflow_commits(full_name)
        print(f" - {commit_count} commits modifying workflows.")

        if commit_count >= MIN_WORKFLOW_COMMITS:
            print(f" ✅ {html_url}")

if __name__ == "__main__":
    main()