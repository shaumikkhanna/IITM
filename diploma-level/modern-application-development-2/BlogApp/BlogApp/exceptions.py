import json
from flask import make_response
from werkzeug.exceptions import HTTPException

class NotFoundError(HTTPException):
    def __init__(self, status_code, error_message):
        message={"error_message": error_message}
        self.response=make_response(json.dumps(message), status_code)

class ValidationError(HTTPException):
    def __init__(self, status_code, error_message, error_code):
        message={"error_message": error_message, "error_code": error_code}
        self.response=make_response(json.dumps(message), status_code)

class InternalError(HTTPException):
    def __init__(self):
        message={"message": "Internal Server Error"}
        self.response = make_response(json.dumps(message), 500)

class AuthError(HTTPException):
    def __init__(self, error_message, error_code):
        message={"error_code": error_code, "error_message": error_message}
        self.response=make_response(message,401)