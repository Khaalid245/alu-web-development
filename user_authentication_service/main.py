#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'alice@example.com'
password = 'AlicePwd123'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("kampala@email.com"))
