from werkzeug.exceptions import HTTPException
from flask import make_response


class SchemaValidationError(HTTPException):
	def __init__(self, message, status_code):
		self.response = make_response(message, status_code)

class NotFoundError(HTTPException):
	def __init__(self, message, status_code):
		self.response = make_response(message, status_code)

class BusinessValidationError(HTTPException):
	def __init__(self, error_code, error_message, status_code):
		message = {'error_code': error_code, 'error_message': error_message}
		self.response = make_response(message, status_code)