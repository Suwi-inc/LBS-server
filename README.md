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
Move into the root directory
```sh
cd .. 
```
### Step 1: Build
```sh
docker build -t 'your_image_name' .   
```
### Step 2: Run
```sh
docker run -p 5000:5000 -e DB_URI='Postgres_DB_connect_string_here' 'your_image_name' 
```
# File structure

```
LBS Server.
│   .dockerignore
│   .gitignore
│   .pre-commit-config.yaml
│   Dockerfile
│   README.md
│   requirements.txt
│   ruff.toml
└───app
    │   .env
    │   app.py
    │   config.py
    │   
    ├───main
    │   │   DataObjects.py
    │   │   __init__.py
    │   │   
    │   ├───controller
    │   │   │   admin_route.py
    │   │   │   gsm_cell.py
    │   │   │   wifi_network.py
    │   │   │   __init__.py
    │   │     
    │   │   
    │   │           
    │   ├───location
    │   │       triangulation.py
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
    │       │   admin_service.py
    │       │   gsm_service.py
    │       │   wifi_service.py
    │                   
    ├───template
    │       exampleRequestData.txt
    │       
    ├───test
```