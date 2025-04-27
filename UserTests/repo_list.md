# Workflow Crawler

Script ...

# Repo List

All repos have been extracted from a public pool

## Python

* https://github.com/wimglenn/johnnydep 
* https://github.com/profusion/sgqlc/ 
* https://github.com/nervosnetwork/rfcs/blob 
* https://github.com/blackholll/loonflow
* https://github.com/gramaziokohler/roslibpy
* https://github.com/GeoStat-Framework/GSTools
* https://github.com/nosarthur/gita
* https://github.com/adafruit/Adafruit_Blinka
* https://github.com/domainaware/parsedmarc
* https://github.com/aegirhall/console-menu

## Java

https://github.com/jenkinsci/jenkinsfile-runner
https://github.com/GoogleContainerTools/jib
https://github.com/kennytv/Maintenance
https://github.com/mayankmetha/Rucky
https://github.com/alibaba/COLA
https://github.com/alibaba/easyexcel
https://github.com/elastic/apm-agent-java
https://github.com/jhipster/prettier-java
https://github.com/GrapheneOS/Auditor
https://github.com/jakartaee/rest

## JavaScript

https://github.com/CodingTrain/Toy-Neural-Network-JS
https://github.com/brentvollebregt/auto-py-to-exe
https://github.com/jaywcjlove/mocker-api
https://github.com/cracker0dks/whiteboard
https://github.com/iamtraction/google-translate
https://github.com/pubkey/eth-crypto
https://github.com/catdad/canvas-confetti
https://github.com/FreeTubeApp/FreeTube
https://github.com/CakeWP/block-options
https://github.com/circlefin/stablecoin-evm

## Ruby

https://github.com/davishmcclurg/json_schemer
https://github.com/piotrmurach/tty-markdown
https://github.com/Shopify/deprecation_toolkit
https://github.com/daveverwer/iOSDevDirectory
https://github.com/discourse/prometheus_exporter
https://github.com/blackcandy-org/blackcandy
https://github.com/davishmcclurg/json_schemer

## Shell Scripts

https://github.com/dappnode/DAppNode
https://github.com/readdle/swift-android-toolchain
https://github.com/jordanwilson230/kubectl-plugins

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

# User Tests