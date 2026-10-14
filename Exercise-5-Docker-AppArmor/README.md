# Exercise 5: Docker Security with AppArmor and Python

## Objective
To explore Docker container security using AppArmor profiles and the Docker SDK for Python.

## Technologies Used
- Docker Desktop
- Python
- Flask
- Docker SDK for Python
- Ubuntu 24.04 on WSL 2

## Tasks Completed

### Task 1: Flask Application
Created a Flask application that returns a welcome message on port 5000.

### Task 2: Docker Image
Created the `flask-apparmor` Docker image using the provided Dockerfile.

### Task 3: AppArmor Environment Check
Checked AppArmor availability in Ubuntu on WSL 2. The AppArmor module reported as loaded, but its filesystem was not mounted. Docker Desktop reported `seccomp` and `cgroupns` security options.

### Task 4: Docker SDK
Created and executed `apply_apparmor.py` to build the image, request the `apparmor=my-apparmor-profile` security option, inspect the container configuration, and clean up the container.

The script reported the configured security option. Actual AppArmor enforcement was not independently verified.

### Task 5: Restricted-Action Tests
Created and executed `test_restricted_actions.py`.

| Test | Observed result |
|---|---|
| Read `/etc/passwd` | Exit code 0 — allowed |
| Execute `/bin/bash --version` | Exit code 0 — allowed |

The tests did not demonstrate the expected restrictions. The environment's AppArmor enforcement needs to be configured and verified before claiming that these actions are blocked.

## Screenshots
- `screenshots/01-flask-app-running.png` — Flask application response

Add any additional screenshots captured during the Docker SDK and restricted-action tests.

## Result
The Flask application was containerized successfully, and the Docker SDK scripts executed. The requested security option was accepted by Docker, but enforcement of the custom AppArmor profile remains unverified.
