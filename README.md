# Chess Tournament Management System

This project is a backend system to manage a chess tournament built with Django and Django REST framework.

## Features

- User Authentication and Authorization using JWT
- Player Management (CRUD operations)
- Tournament Management
- Match Management with Swiss-system pairing
- Leaderboard calculation
- API Documentation with Swagger

## Requirements

- Python 3.12.1
- Django 5.0.2
- Django REST framework
- drf-yasg for API documentation
- djangorestframework-simplejwt for JWT authentication

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ShahloSafarova/Chess_tournament.git
    ```

2. Create and activate the virtual environment:

    If you already have a virtual environment named `env`:

    ```bash
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

    If you need to create a new one:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the project root and add the following:

    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

5. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the API documentation:

    - Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## API Endpoints

### Authentication

- **POST** `/api/register/` - Register a new user
- **POST** `/api/login/` - Login and obtain JWT tokens

### Players

- **GET** `/api/players/` - List all players
- **POST** `/api/players/` - Create a new player
- **GET** `/api/players/{id}/` - Retrieve a player by ID
- **PUT** `/api/players/{id}/` - Update a player by ID
- **DELETE** `/api/players/{id}/` - Delete a player by ID

### Tournaments

- **GET** `/api/tournaments/` - List all tournaments
- **POST** `/api/tournaments/` - Create a new tournament
- **GET** `/api/tournaments/{id}/` - Retrieve a tournament by ID
- **PUT** `/api/tournaments/{id}/` - Update a tournament by ID
- **DELETE** `/api/tournaments/{id}/` - Delete a tournament by ID

### Matches

- **GET** `/api/matches/` - List all matches
- **POST** `/api/matches/` - Create a new match
- **GET** `/api/matches/{id}/` - Retrieve a match by ID
- **PUT** `/api/matches/{id}/` - Update a match by ID
- **DELETE** `/api/matches/{id}/` - Delete a match by ID

### Leaderboard

- **GET** `/api/leaderboard/{tournament_id}/` - Retrieve the leaderboard for a specific tournament
