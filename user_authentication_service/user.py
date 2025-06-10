#!/usr/bin/env python3
"""
This module contains the definition of the User model.
The User model includes attributes for email, hashed password,
session ID, and reset token, and provides methods for hashing
and verifying passwords using bcrypt.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()


class User(Base):
    """
    User model for the users table.

    Attributes:
        id (int): The primary key of the user.
        email (str): The email address of the user.
        hashed_password (str): The hashed password of the user.
        session_id (str): The session ID of the user.
        reset_token (str): The reset token for the user.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def hash_password(self, password):
        """
        Hashes a password using bcrypt and sets the hashed_password attribute.

        Args:
            password (str): The password to hash.
        """
        self.hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

    def verify_password(self, password):
        """
        Verifies the password against the stored hashed password.

        Args:
            password (str): The password to verify.

        Returns:
            bool: True if the password matches the stored hashed password,
                  False otherwise.
        """
        return bcrypt.checkpw(
            password.encode('utf-8'), self.hashed_password.encode('utf-8')
        )
