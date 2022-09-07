from flask import request
from flask_restful import Resource, fields, marshal_with
from database import db
from models import *
from validation import *


fields_course_resource = {
	"course_id": fields.Integer,
	"course_name": fields.String,
	"course_code": fields.String,
	"course_description": fields.String
}

fields_student_resource = {
	"student_id": fields.Integer,
	"first_name": fields.String,
	"last_name": fields.String,
	"roll_number": fields.String
}

fields_enrollment_resource = {
	"enrollment_id": fields.Integer,
	"student_id": fields.Integer,
	"course_id": fields.Integer
}

class CourseAPI(Resource):
	@marshal_with(fields_course_resource)
	def get(self, course_id):
		# Course not found 404 error
		specific_course = Course.query.filter_by(course_id=course_id).first()
		if specific_course is None:
			raise NotFoundError(message='', status_code=404)
		
		else:
			return specific_course
	
	@marshal_with(fields_course_resource)
	def post(self):
		# Getting request data
		new_course_dict = request.json
		new_course_name = new_course_dict.get('course_name', None)
		new_course_code = new_course_dict.get('course_code', None)
		new_course_description = new_course_dict.get('course_description', None)

		# Bad request 400 validation
		if type(new_course_name) != str:
			raise BusinessValidationError(error_code='COURSE001', error_message='Course Name is required and should be string.', status_code=400)
		if type(new_course_code) != str:
			raise BusinessValidationError(error_code='COURSE002', error_message='Course Code is required and should be string.', status_code=400)
		if new_course_description is not None and type(new_course_description) != str:
			raise BusinessValidationError(error_code='COURSE003', error_message='Course Description should be string.', status_code=400)

		# Course code already exists 409 error
		all_course_codes = [c.course_code for c in Course.query.all()]
		if new_course_code in all_course_codes:
			raise SchemaValidationError(message='', status_code=409)

		# Adding to database
		try:
			new_course = Course(course_name=new_course_name, course_code=new_course_code, course_description=new_course_description)
			db.session.add(new_course)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return new_course, 201

	@marshal_with(fields_course_resource)
	def put(self, course_id):
		# Course not found 404 error
		specific_course = Course.query.filter_by(course_id=course_id).first()
		if specific_course is None:
			raise NotFoundError(message='', status_code=404)
		
		# Getting request data
		updated_course_dict = request.json
		updated_course_name = updated_course_dict.get('course_name', None)
		updated_course_code = updated_course_dict.get('course_code', None)
		updated_course_description = updated_course_dict.get('course_description', None)

		# Bad request 400 validation
		if type(updated_course_name) != str:
			raise BusinessValidationError(error_code='COURSE001', error_message='Course Name is required and should be string.', status_code=400)
		if type(updated_course_code) != str:
			raise BusinessValidationError(error_code='COURSE002', error_message='Course Code is required and should be string.', status_code=400)
		if updated_course_description is not None and type(updated_course_description) != str:
			raise BusinessValidationError(error_code='COURSE003', error_message='Course Description should be string.', status_code=400)

		# Updating database
		try:
			specific_course.course_name = updated_course_name
			specific_course.course_code = updated_course_code
			specific_course.course_description = updated_course_description
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return specific_course

	def delete(self, course_id):
		# Course not found 404 error
		specific_course = Course.query.filter_by(course_id=course_id).first()
		if specific_course is None:
			raise NotFoundError(message='', status_code=404)
		
		try:
			db.session.delete(specific_course)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return '', 200


class StudentAPI(Resource):
	@marshal_with(fields_student_resource)
	def get(self, student_id):
		# Student not found 404 error
		specific_student = Student.query.filter_by(student_id=student_id).first()
		if specific_student is None:
			raise NotFoundError(message='', status_code=404)
		
		else:
			return specific_student

	@marshal_with(fields_student_resource)
	def post(self):
		# Getting request data
		new_student_dict = request.json
		new_first_name = new_student_dict.get('first_name', None)
		new_last_name = new_student_dict.get('last_name', None)
		new_roll_number = new_student_dict.get('roll_number', None)

		# Bad request 400 validation
		if type(new_roll_number) != str:
			raise BusinessValidationError(error_code='STUDENT001', error_message='Roll Number is required and should be string.', status_code=400)
		if type(new_first_name) != str:
			raise BusinessValidationError(error_code='STUDENT002', error_message='First Name is required and should be string.', status_code=400)
		if new_last_name is not None and type(new_last_name) != str:
			raise BusinessValidationError(error_code='STUDENT003', error_message='Last Name is String', status_code=400)

		# Student already exists 409 error
		all_roll_numbers = [s.roll_number for s in Student.query.all()]
		if new_roll_number in all_roll_numbers:
			raise SchemaValidationError(message='', status_code=409)

		# Adding to database
		try:
			new_student = Student(first_name=new_first_name, last_name=new_last_name, roll_number=new_roll_number)
			db.session.add(new_student)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return new_student, 201

	@marshal_with(fields_student_resource)
	def put(self, student_id):
		# Student not found 404 error
		specific_student = Student.query.filter_by(student_id=student_id).first()
		if specific_student is None:
			raise NotFoundError(message='', status_code=404)
		
		# Getting request data
		updated_student_dict = request.json
		updated_roll_number = updated_student_dict.get('roll_number', None)
		updated_first_name = updated_student_dict.get('first_name', None)
		updated_last_name = updated_student_dict.get('last_name', None)

		# Bad request 400 validation
		if type(updated_roll_number) != str:
			raise BusinessValidationError(error_code='STUDENT001', error_message='Roll Number is required and should be string.', status_code=400)
		if type(updated_first_name) != str:
			raise BusinessValidationError(error_code='STUDENT002', error_message='First Name is required and should be string.', status_code=400)
		if updated_last_name is not None and type(updated_last_name) != str:
			raise BusinessValidationError(error_code='STUDENT003', error_message='Last Name is String', status_code=400)

		# Updating database
		try:
			specific_student.roll_number = updated_roll_number
			specific_student.first_name = updated_first_name
			specific_student.last_name = updated_last_name
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return specific_student

	def delete(self, student_id):
		# Course not found 404 error
		specific_student = Student.query.filter_by(student_id=student_id).first()
		if specific_student is None:
			raise NotFoundError(message='', status_code=404)
		specific_enrollments = Enrollments.query.filter_by(student_id=student_id).all()
		
		try:
			db.session.delete(specific_student)
			for specific_enrollment in specific_enrollments:
				db.session.delete(specific_enrollment)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return '', 200


class EnrollmentsAPI(Resource):
	@marshal_with(fields_enrollment_resource)
	def get(self, student_id):
		# Invalid student 400 error
		specific_student = Student.query.filter_by(student_id=student_id).first()
		if specific_student is None:
			raise BusinessValidationError(error_code='ENROLLMENT002', error_message='Student does not exist.', status_code=400)

		specific_enrollments = Enrollments.query.filter_by(student_id=student_id).all()	

		# No enrollments 404 error
		if not specific_enrollments:
			raise NotFoundError(message='', status_code=404)

		return specific_enrollments

	@marshal_with(fields_enrollment_resource)
	def post(self, student_id):
		# Student not found 404 error
		specific_student = Student.query.filter_by(student_id=student_id).first()
		if specific_student is None:
			raise NotFoundError(message='', status_code=404)

		# Getting request data
		course_id = request.json.get('course_id', None)

		# Bad request 400 error
		if type(course_id) != int:
			raise BusinessValidationError(error_code='ENROLLMENT003', error_message='Course Code is required and should be string.', status_code=400)

		try:
			new_enrollment = Enrollments(student_id=student_id, course_id=course_id)
			db.session.add(new_enrollment)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			print('Successfully commited')
			db.session.commit()

		return new_enrollment, 201

	def delete(self, student_id, course_id):
		# Invalid student or course 400 error
		specific_student = Student.query.filter_by(student_id=student_id).first()
		specific_course = Course.query.filter_by(course_id=course_id).first()
		if specific_course is None:
			raise BusinessValidationError(error_code='ENROLLMENT001', error_message='Course does not exist.', status_code=400)
		if specific_student is None:
			raise BusinessValidationError(error_code='ENROLLMENT002', error_message='Student does not exist.', status_code=400)

		# Enrollment not found 404
		specific_enrollment = Enrollments.query.filter_by(student_id=student_id, course_id=course_id).first()	
		if specific_enrollment is None:
			raise NotFoundError(message='', status_code=404)

		try:
			db.session.delete(specific_enrollment)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return '', 200

