import os
import subprocess
import json

REPOS_FOLDER = "repos"
FIXNPUSH_OUTPUT_FOLDER = "fixnpush_outputs"

def clone_repo(repo_url):
    os.makedirs(REPOS_FOLDER, exist_ok=True)
    repo_name = repo_url.split("/")[-1]
    dest_path = os.path.join(REPOS_FOLDER, repo_name)
    if not os.path.exists(dest_path):
        subprocess.run(["git", "clone", repo_url, dest_path])
    else:
        print(f"Repo {repo_name} already cloned.")
    return dest_path

def run_fixnpush(repo_path):
    os.makedirs(FIXNPUSH_OUTPUT_FOLDER, exist_ok=True)
    output_file = os.path.join(FIXNPUSH_OUTPUT_FOLDER, os.path.basename(repo_path) + "_fixnpush.json")
    command = ["fixnpush", "--output-json", output_file, repo_path]
    subprocess.run(command)
    return output_file

def download_and_run_fixnpush():
    with open("repos_list.json", "r") as f:
        repos = json.load(f)

    for repo in repos:
        repo_url = repo["html_url"]
        print(f"Processing {repo_url}...")
        local_path = clone_repo(repo_url)
        run_fixnpush(local_path)

if __name__ == "__main__":
    download_and_run_fixnpush()