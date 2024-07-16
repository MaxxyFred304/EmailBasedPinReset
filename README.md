# Password Reset Project

This project is a Django application with a RESTful API that allows users to reset their PIN using their email address.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Reset PIN using email address.
- Email validation and sending instructions.
- Simple API endpoint for PIN reset requests.

## Requirements

- Python 3.6+
- Django 3.2+
- djangorestframework 3.12+

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/maxxyfred304/password-reset-project.git
    cd password-reset-project
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project and add your environment variables:

    ```
    SECRET_KEY=your-secret-key
    DEBUG=True
    ```

5. Apply the migrations:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Configuration

### Email Backend

For development, use the console email backend to print email content to the console:

```python
# passwordproject/settings.py

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'your-email@example.com'
```

For production, configure an SMTP email backend:

```python
# passwordproject/settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'
```

## Usage

To reset a PIN, send a POST request to the API endpoint with the user's email address.

### Example Request:

```sh
curl -X POST http://127.0.0.1:8000/api/reset-pin/ -H "Content-Type: application/json" -d '{"email": "user@example.com"}'
```

### Example Response:

```json
{
    "message": "Pin reset instructions sent"
}
```

## API Endpoints

- `POST /api/reset-pin/` - Reset PIN using email address.

## Testing

1. Run the development server:

    ```sh
    python manage.py runserver
    ```

2. Send a test request using `curl`:

    ```sh
    curl -X POST http://127.0.0.1:8000/api/reset-pin/ -H "Content-Type: application/json" -d '{"email": "user@example.com"}'
    ```

3. Check the console output for the email content.

## Project Structure

```
password-reset-project/
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── passwordproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---