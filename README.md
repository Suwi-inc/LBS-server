# LBS-server

# Installation Guide
## Build and Run
### Step 1. Clone the github repo to your prefered directory using
```
git clone https://github.com/Suwi-inc/LBS-server.git
``` 
### Step 2. Inside the repository directory install the project dependencies
```sh
pip install -r requirements.txt
```
### Step 3: Create .env

The project depends on some config that it expects to be provided from a .env file at the `app` directory. 
```sh
cd app
``` 
Here is the expected content of the file
```env
DB_URI='Postgres_DB_connect_string_here'
```
### Step 4: Run Migrations

```sh
flask db init
flask db migrate
flask db upgrade
```
### Step 5: Run the program
Within the `app` directory
```sh
flask --app app run   
```
# Build and Run on Docker
Required docker version: >=4.25.2
Before running, place an .env file in the root directory
```sh
docker compose up --build -d
```
# Project File structure 

```
LBS-Server
│   .dockerignore
│   .gitignore
│   .pre-commit-config.yaml
│   docker-compose.yml
│   README.md
│   ruff.toml
│   scripttorun.txt
│   test_backup.sql
│  
├───.github
│   └───workflows
│           docker-image.yml
│           
└───LBS
    │   config.py                                           # place our config here to run locally
    │   app.py
    │   Dockerfile
    │   requirements.txt
    │   
    ├───main
    │   │   DataObjects.py
    │   │   __init__.py
    │   │   
    │   ├───controller
    │   │   │   admin_route.py
    │   │   │   gsm_cell.py
    │   │   │   location.py
    │   │   │   wifi_network.py
    │   │   │   __init__.py
    │   │   │   
    │   │   
    │   │           
    │   ├───model
    │   │   │   models.py
    │   │   │   
    │   │   └───__pycache__
    │   │           models.cpython-311.pyc
    │   │           
    │   ├───schemas
    │   │       DataBaseSchema.SQL
    │   │       
    │   ├───service
    │   │   │   admin_service.py
    │   │   │   gsm_service.py
    │   │   │   wifi_service.py
    │   │   │   
    │   │   └───__pycache__
    │   │           admin_service.cpython-311.pyc
    │   │           gsm_service.cpython-311.pyc
    │   │           wifi_service.cpython-311.pyc
    │   │           
    │   ├───utils
            │   data_validator.py
```