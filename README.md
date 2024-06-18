# LBS-server

# Installation Guide

## Build and Run

### Step 1. Clone the github repo
```sh
git clone https://github.com/Suwi-inc/LBS-server.git
cd LBS-server
```

### Step 2. Install [Docker](https://docs.docker.com/engine/install/)

### Step 3: Create a .env file in the root of the project

```.env
POSTGRES_USER={username}
POSTGRES_PASSWORD={password}
POSTGRES_DB={database}
SECRET_KEY={string}
REMOTE_IP={host}
REMOTE_DB_PORT={port}
DB_URI=postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}
```

### Step 4: Run docker compose
```sh
docker compose up --build -d
```

### Step 4a: TBD



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
