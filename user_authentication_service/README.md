# User Authentication Service

## Overview
The User Authentication Service is a service that handles user authentication and authorization for a web application. It provides functionality for user registration, login, logout, and password reset.

## Features
- User registration: Allows users to create new accounts by providing their email address and password.
- User login: Authenticates users by verifying their credentials and generates a session token for subsequent requests.
- User logout: Invalidates the session token and logs the user out.
- Password reset: Allows users to reset their password by sending a password reset email.

## Architecture
The User Authentication Service follows a client-server architecture. It exposes a RESTful API for client applications to interact with. The service stores user data in a database and uses encryption algorithms to securely store and validate passwords.


## Getting Started
To use the User Authentication Service in your project, follow these steps:

1. Install the necessary dependencies.
    - pip3 install bcrypt
2. Configure the database connection.
3. Set up the necessary environment variables.
4. Start the service.

## API Reference
- declare API routes in a Flask app
