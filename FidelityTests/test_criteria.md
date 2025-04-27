# Fidelity Tests

## 🧱 Workflow Structure

This repos are aimed to test the fundamental building blocks of any workflow:

    * name: Custom workflow name
    * on: Trigger types (e.g., push, pull_request, workflow_dispatch, schedule, release)
    * jobs: Single vs. multiple jobs
    * defaults: Default shell or working directory
    * env: Global environment variables
    * inputs:
    * outputs: 

https://github.com/nervosnetwork/rfcs/blob


## 🔁 Job Configuration

This repos are aimed to test possible job configurations:

    * runs-on: OS variations (ubuntu-latest, windows-latest, macos-latest, self-hosted)
    * needs: Job dependencies (job graphs)
    * strategy.matrix: Matrix builds with multiple OS/versions
    * continue-on-error: Conditional error toleration
    * timeout-minutes: Execution limits
    * if: Conditional job execution
    * concurrency: Job-level concurrency limits

## 🧩 Step Syntax and Types

    * uses: Actions from the marketplace (actions/checkout@v3, custom actions)
    * run: Shell commands, including multiline (|)
    * with: Action inputs (e.g., with: node-version: 16)
    * env: Step-specific environment variables
    * shell: Custom shell configuration (bash, pwsh, python, etc.)
    * id: Step IDs for referencing outputs
    * name: Custom step names for readability
    * continue-on-error: Step-level error control
    * working-directory: Scoped directories for execution

## 🧠 Conditionals and Expressions

    * if: Workflow/job/step conditionals using GitHub Expressions
    * steps.<id>.outputs: Accessing previous step outputs
    * Expressions like github.ref, github.event_name, contains(...), startsWith(...), etc.

## 🧰 Artifacts and Caching

    * actions/upload-artifact, download-artifact
    * actions/cache: Handling cache keys, restore/save paths

## 🔒 Secrets and Contexts

    * secrets.*: Accessing secrets (must test both existing and missing ones)
    * github.*: Built-in context variables (e.g., github.sha, github.actor)
    * env.*: From global or job-level env blocks

## ♻️ Custom/Reusable Workflows

    * uses: ./path/to/local-action
    * uses: ./.github/workflows/another-workflow.yml (reusable workflows)
    * inputs and outputs of reusable workflows
    * workflow_call, workflow_run: Reusable triggers and nesting

## Docker and Container Jobs

    * container: image: node:14: Running job inside Docker containers
    * Services block: e.g., MySQL, Redis using services: syntax