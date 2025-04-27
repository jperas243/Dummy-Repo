import requests
import time
import os
import json
from urllib.parse import quote

# === CONFIG ===
GITHUB_TOKEN = "your_token_here"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}
OUTPUT_FOLDER = "workflow_outputs"

def search_repositories(language="Python", min_stars=100, max_repos=50):
    repos = []
    page = 1
    while len(repos) < max_repos:
        query = f"language:{language} stars:>={min_stars}"
        url = f"https://api.github.com/search/repositories?q={quote(query)}&sort=stars&order=desc&per_page=30&page={page}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            break
        data = resp.json()
        repos.extend(data.get("items", []))
        if len(data.get("items", [])) < 30:
            break
        page += 1
        time.sleep(1)
    return repos[:max_repos]

def list_workflows(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/actions/workflows"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        return []
    return resp.json().get("workflows", [])

def download_workflow_runs(repo_full_name, workflow_id):
    url = f"https://api.github.com/repos/{repo_full_name}/actions/workflows/{workflow_id}/runs"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        return []
    return resp.json().get("workflow_runs", [])

def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def crawl_workflows():
    repos = search_repositories()
    print(f"Found {len(repos)} repositories.")

    for repo in repos:
        full_name = repo["full_name"]
        workflows = list_workflows(full_name)
        for wf in workflows:
            runs = download_workflow_runs(full_name, wf["id"])
            if runs:
                filename = f"{OUTPUT_FOLDER}/{full_name.replace('/', '__')}__{wf['name'].replace(' ', '_')}.json"
                save_json(filename, runs)
                print(f"Saved {len(runs)} runs for {full_name} - {wf['name']}")
            time.sleep(0.5)

    save_json("repos_list.json", repos)
    print("Saved repository list.")

if __name__ == "__main__":
    crawl_workflows()