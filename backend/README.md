# Pillow - Backend

The backend of the app is responsible for handling server-side operations and processing data. It acts as the bridge between the front-end interface and the database.

## Setup

- **Environmental Variables**: You should set the following environmental variables and create both database and user on MySQL:
    ```bash
    DB_NAME_PILLOW=pillow # Create a database first
    DB_USER_PILLOW=your_username # Create this user if does not exist with all priviledges to this database
    DB_PASS_PILLOW=user_pass # User password for this database
    DB_HOST_PILLOW=localhost
    DB_PORT_PILLOW=3306
    ```
- **Migrations**: After setting all environmental variables and the database, migrate all tables to MySQL
    ```bash
    python3 -m manage makemigrations # Checks if there are any migrations to make
    python3 -m manage migrate # Migrate
    ```

## Features

- **API Endpoints**: The backend exposes a set of API endpoints that allow the front-end to communicate with the server. These endpoints handle various operations such as retrieving data, updating records, and deleting records.

- **Authentication and Authorization**: The backend implements authentication and authorization mechanisms to ensure that only authorized users can access certain resources or perform specific actions.

## Technologies Used

- **Programming Language**: The backend is implemented using Python.

- **Framework**: Django

- **Database**: The backend interacts with a database management system (DBMS) like SQLite3 for development and MySQL for production.

- **API Documentation**: The backend may include API documentation using tools like Postman to provide detailed information about the available endpoints, request/response formats, and authentication requirements.

