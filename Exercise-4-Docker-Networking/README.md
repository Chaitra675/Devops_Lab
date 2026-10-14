# Exercise 4: Docker Networking with Multiple Containers

## Objective
To create a custom Docker bridge network and run multiple containers that communicate with each other using container names.

## Technologies Used
- Docker
- Python
- Flask
- MySQL
- Redis

## Implementation
1. Created a custom bridge network named `my-bridge-net`.
2. Built a Docker image named `flask-api`.
3. Started MySQL, Redis, and Flask containers on the same bridge network.
4. Exposed the Flask API on port 5001.
5. Tested connectivity from the Flask container to MySQL and Redis using `ping`.

## API Endpoint

**URL:** `http://localhost:5001/about`

**Method:** GET

**Response:**
```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

## Network Connectivity
Both MySQL and Redis were successfully reachable from the Flask container by their container names. Both ping tests completed with 0% packet loss.

## Screenshots
- `screenshots/03-containers-running.png` — Running containers
- `screenshots/04-network-connectivity.png` — Connectivity tests
- `screenshots/05-flask-api-response.png` — Flask API response

## Result
Successfully created a custom Docker bridge network and verified communication between the Flask, MySQL, and Redis containers.
