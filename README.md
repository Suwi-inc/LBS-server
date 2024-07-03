# LBS-server

# Installation Guide

## Step 1: Clone the github repo
```sh
git clone https://github.com/Suwi-inc/LBS-server.git
cd LBS-server
```

## Step 2: Create a .env file in the root of the project and decide which option is more appropriate
There are 2 entites that the product consists of: python web API and postgreSQL DBMS. 
There are also 3 options to set the environment up:
1. Using docker for both entities
2. Using docker for web API, db is hosted somewhere else
3. No docker, python server and postgres are installed locally

The env file:
```dotenv
# for all cases
DATABASE_USER={the user of the db}
DATABASE_PASSWORD={the user's password}
DATABASE_LBS_NAME={main database name}
DATABASE_LOGGER_NAME={logger database name}
SECRET_KEY={secret key}

# for the 1-st case
DATABASE_HOST_LOCAL_DOCKER={the name of the postgres container}
DATABASE_PORT_LOCAL_DOCKER={the inner port of the postgres container}

# for the 2-nd case
DATABASE_HOST_REMOTE={the ip of the remote server}
DATABASE_PORT_REMOTE={its port}

# for the 3-rd case
DATABASE_HOST_LOCAL_NATIVE={the name of the postgres installed locally (no docker)}
DATABASE_PORT_LOCAL_NATIVE={its port}
DB_URI=postgresql+psycopg2://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST_LOCAL_NATIVE}:${DATABASE_PORT_LOCAL_NATIVE}/${DATABASE_LBS_NAME}
LOGS_DB=postgresql+psycopg2://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST_LOCAL_NATIVE}:${DATABASE_PORT_LOCAL_NATIVE}/${DATABASE_LOGGER_NAME}
```

## Case 1 and 2
### Step 3: Install [Docker](https://docs.docker.com/engine/install/)
### Step 4: Choose the appropriate option in docker-compose.yml lbs service environment section
### Step 5: Run docker compose
```sh
docker compose up --build -d
```
### Step 6: Restore the databases using the dumps (via pgAdmin is fast)

## Case 3
### Step 3: Install Python
### Step 4: Install PostgreSQL
### Step 5: Restore the databases using the dumps (via pgAdmin is fast)
### Step 6: Run the app
```sh
cd LBS
poetry run flask --app app run --host=0.0.0.0
```
