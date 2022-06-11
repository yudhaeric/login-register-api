# Login Register API
## Set Up
1. Install [python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/cli/pip_install/), [venv](https://cloud.google.com/python/docs/setup) and [docker](https://docs.docker.com/get-docker/) (optional)
2. Clone the repository
## Run the App (without docker)
1. Create a virtual env
    ```
    pip install virtualenv
    ```
    ```
    virtualenv env
    ```
    ```
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```
    ```
    env/Scripts/activate
    ```
2. Run installation
    ```
    pip install -r requirements.txt
    ```
3. Create file .env & connect to your database 
    ```
    FLASK_APP = server.py
    FLASK_ENV = development
    
    DB_HOST=
    DB_DATABASE=
    DB_USERNAME=
    DB_PASSWORD=
    ```
5. Run the app 
    ```
    flask run
    ```
