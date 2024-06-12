# LBS-server

# Installation Guide

Supported installation ways:
* Docker (recommended)
* Local

# Docker installation

## Build and Run containers

### Step 1. Clone the github repo to your preferred directory
```sh
git clone https://github.com/Suwi-inc/LBS-server.git
cd LBS-server
```

### Step 2. Install Docker if it is not installed
https://docs.docker.com/engine/install/

### Step 3: Create .env file
```sh
echo "SECRET_KEY='SECRET_KEY'" > LBS/.env
```
The `SECRET_KEY` environmental variable is used for generating *JWT*.

### Step 4: Define environment variables
```sh
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=pass
export POSTGRES_DB=postgres
export REMOTE_DB_PORT=5433
```
It is possible to change any of these values.

### Step 5: Run docker compose
Run this command when you update the server
```sh
docker compose up --build -d
```

## Migrate database

### Step 1: Extract database dump
The dump containes of `.dat.gz` files. Extract them in the repository directory. This way, they will be visible in postgres container.

### Step 2: Execute shell in postgres container
```sh
docker container ps
```
Take the identifier of the postgres container.
```sh
docker exec -it <id> bash
```

### Step 3: Locate the directory with dump
The repository directory is mounted at `docker-entrypoint-initdb.d`. Found there the directory with dump files and remember it.

### Step 4: Login to psql
If you didn't change variables, the *username* will be `postgres`.
```sh
su <username>
psql --username=<username>
```

### Step 5: Choose the database and clean it
If you didn't change variables, the *database* will be `postgres`.
```sh
\c <database>
```

Check, if there are tables. If yes, delete them.
```
\dt
```

### Step 6: Restore
Here *path* is path to the dump.
```sh
ps_restore <path>
```

## Stop containers
```sh
docker compose down
```

# Local installation

## Prepare postgresql server

TODO: Decide in which depth to explain this.

* Do not use special characters in the password

### Step 1: Prepare DB_URI variable

Create `DB_URI` environmental variable using following template:
`DB_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${REMOTE_IP}:${REMOTE_DB_PORT}/${POSTGRES_DB}`

```sh
export DB_USI=<value>
```

## Build and Run server

### Step 1: Install python and poetry
The installation depends on your distribution.

### Step 2: Install python 3.11 if you version is lower
Installation using `apt`.
```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
rm LBS/poetry.lock
poetry env use python3.11
```
This will choose `python3.11` as default executable for poetry.

### Step 3: Create .env file
```sh
echo "SECRET_KEY='SECRET_KEY'" > LBS/.env
```
The `SECRET_KEY` environmental variable is used for generating *JWT*.

### Step 4: Install dependencies
```sh
cd LBS
poetry install
```

### Step 5: Migrate
```sh
poetry run flask db init
poetry run flask db migrate
poetry run flask db upgrade
```

### Step 6: Run the application
```sh
poetry run flask --app app run
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
