# Agent-Project-Backend

## Introduction

This is the backend for Agent project.

## Installation

### Prerequisites

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Git](https://git-scm.com/)
* [SSH](https://www.ssh.com/ssh/protocol/)

### Steps

1. Clone this repository.

2. Go into the cloned repository:
   
3. Start the backend using prepared .sh script:

    ```bash
    bash dockercompose.sh dev up --build
    ```

- (Optional) If you want to run the backend in the background, use the following command:

    ```bash
    bash dockercompose.sh dev up --build -d
    ```
  
- (Optional) If you want to run the backend in the background and see the logs, use the following command:

    ```bash
    bash dockercompose.sh dev up --build -d && bash dockercompose.sh dev logs -f
    ```
  
- (Optional) If you want to run the backend in prod server, use the following command:

    ```bash
    bash dockercompose.sh prod up --build
    ```
  
4. Open the backend in your browser:

    ```bash
    http://localhost:8011/admin/
    ```
   
5. Login with the default credentials:

    ```bash
    Email: admin@berkaymizrak.com
    Password: 123456@@
    ```
   
6. Enjoy!

## Some Commands for Development

### To make migrations in continuous development, RUN:
- makemigrations
```bash
docker exec -it app_agent_dev python manage.py makemigrations
```

- migrate
```bash
docker exec -it app_agent_dev python manage.py migrate
```

### Collect static for style and js changes:
```bash
docker exec -it app_agent_dev python manage.py collectstatic
```
OR
```bash
docker exec -it app_agent_dev python manage.py collectstatic --noinput
```

### Update requirements after adding new packages:
```bash
docker exec -it app_agent_dev pip freeze > requirements.txt
```
