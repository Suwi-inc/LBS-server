# LBS-server

# Installation Guide

## Build and Run

### Step 1. Clone the github repo to your preferred directory
```sh
git clone https://github.com/Suwi-inc/LBS-server.git
cd LBS-server
```

### Step 2. Install Docker if it is not installed
https://docs.docker.com/engine/install/

### Step 3: Create .env file

The project depends on some config that it expects to be provided from an .env file at the `LBS` directory.
```sh
cd LBS
```

Here is the expected content of the file:
```sh
SECRET_KEY='your_auth_secret'
```

# Step 4: Define environment variables
```sh
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=pass
export POSTGRES_DB=postgres
export SECRET_KEY=SECRET_KEY
export REMOTE_DB_PORT=5433
```

### Step 5: Run docker compose
Run this command when you update the server
```sh
docker compose up --build -d
```

## Stop
```sh
docker compose down
```

# Project File structure

```
LBS-Server
│   .dockerignore
│   .gitignore
│   .pre-commit-config.yaml
│   docker-compose.yml
|   LBS-Endpoints.postman_collection.json
│   README.md
│   ruff.toml
│
├───.github
│   └───workflows
│       └───docker-image.yml
│
└───LBS
    │   .env
    │   app.py
    │   Dockerfile
    |   poetry.lock
    |   pyproject.toml
    │   requirements.txt
    │
    └───main
        │   __init__.py
        │   DataObjects.py
        │
        ├───auth
        |   |   __init__.py
        |   |   auth_guard.py
        |   |   auth_provider.py
        |   └───jwt_handler.py
        │
        ├───controller
        │   │   __init__.py
        │   │   admin_route.py
        │   │   device_route.py
        │   │   gsm_cell.py
        │   │   location.py
        │   └───wifi_network.py
        │
        ├───model
        │   └───models.py
        │
        ├───schemas
        │   └───DataBaseSchema.SQL
        │
        ├───service
        │   │   admin_service.py
        │   │   device_service.py
        │   │   gsm_service.py
        │   └───wifi_service.py
        │
        └───utils
            └───data_validator.py
```
