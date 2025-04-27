import os
import json

WORKFLOW_OUTPUTS_FOLDER = "workflow_outputs"
FIXNPUSH_OUTPUT_FOLDER = "fixnpush_outputs"
REPORT_FOLDER = "reports"

def parse_github_runs(workflow_runs):
    parsed = []
    for run in workflow_runs:
        parsed.append({
            "name": run.get("name"),
            "conclusion": run.get("conclusion"),
            "status": run.get("status")
        })
    return parsed

def parse_fixnpush_runs(fixnpush_runs):
    parsed = []
    for run in fixnpush_runs:
        parsed.append({
            "name": run.get("workflow_name"),
            "conclusion": run.get("result")
        })
    return parsed

def compare_runs(github_runs, fixnpush_runs):
    matches = 0
    mismatches = 0

    github_by_name = {run["name"]: run for run in github_runs}
    fixnpush_by_name = {run["name"]: run for run in fixnpush_runs}

    for name, gh_run in github_by_name.items():
        fp_run = fixnpush_by_name.get(name)
        if not fp_run:
            mismatches += 1
            continue
        if gh_run["conclusion"] == fp_run["conclusion"]:
            matches += 1
        else:
            mismatches += 1

    total = matches + mismatches
    fidelity = (matches / total) * 100 if total else 0
    return {
        "matches": matches,
        "mismatches": mismatches,
        "fidelity_score": round(fidelity, 2)
    }

def run_matching():
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    with open("repos_list.json", "r") as f:
        repos = json.load(f)

    reports = []

    for repo in repos:
        repo_name = repo["full_name"].replace("/", "__")

        # Find all related workflow output files
        matches = [f for f in os.listdir(WORKFLOW_OUTPUTS_FOLDER) if f.startswith(repo_name)]
        if not matches:
            continue

        for workflow_file in matches:
            github_output_path = os.path.join(WORKFLOW_OUTPUTS_FOLDER, workflow_file)
            with open(github_output_path, "r") as f:
                github_runs = json.load(f)
            github_parsed = parse_github_runs(github_runs)

            fixnpush_output_path = os.path.join(FIXNPUSH_OUTPUT_FOLDER, repo["name"] + "_fixnpush.json")
            if not os.path.exists(fixnpush_output_path):
                continue
            with open(fixnpush_output_path, "r") as f:
                fixnpush_runs = json.load(f)
            fixnpush_parsed = parse_fixnpush_runs(fixnpush_runs)

            comparison = compare_runs(github_parsed, fixnpush_parsed)
            report = {
                "repo": repo["full_name"],
                "workflow_file": workflow_file,
                **comparison
            }
            reports.append(report)

    # Save report
    report_path = os.path.join(REPORT_FOLDER, "comparison_report.json")
    with open(report_path, "w") as f:
        json.dump(reports, f, indent=2)
    print(f"Saved comparison report to {report_path}")

if __name__ == "__main__":
    run_matching()