from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Link database to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


# MODELS
class Student(db.Model):
	__tablename__ = 'student'
	student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	roll_number = db.Column(db.String, unique=True, nullable=False)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String)
	enrollment = db.relationship('Course', secondary='enrollments')

class Course(db.Model):
	__tablename__ = 'course'
	course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	course_code = db.Column(db.String, unique=True, nullable=False)
	course_name = db.Column(db.String, nullable=False)
	course_description = db.Column(db.String)

class Enrollments(db.Model):
	__tablename__ = 'enrollments'
	enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
	ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)


# CONTROLLERS
@app.route('/', methods=['GET'])
def home():
	students = Student.query.all()
	
	if students:
		return render_template(
			'home_list.jinja2.html', 
			students=students
			)
	# for no students
	else:
		return render_template(
			'home_empty.jinja2.html'
			)


@app.route('/student/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template(
			'create.html'
			)

	if request.method == 'POST':
		# getting form data
		new_roll_number = request.form.get('roll')

		# Redirect if duplicate student
		all_roll_numbers = [s.roll_number for s in Student.query.all()]
		if new_roll_number in all_roll_numbers:
			return render_template(
				'create_already_exists.html'
				)
		
		new_first_name = request.form.get('f_name')
		new_last_name = request.form.get('l_name')
		new_courses_ids = [int(c[-1]) for c in request.form.getlist('courses')]

		# add and commit in database
		try:
			# new student record
			new_student = Student(roll_number=new_roll_number, first_name=new_first_name, last_name=new_last_name)
			db.session.add(new_student)
			db.session.flush()

			# multiple enrollment records
			new_student_id = new_student.student_id
			for new_course_id in new_courses_ids:
				new_enrollment = Enrollments(estudent_id=new_student_id, ecourse_id=new_course_id)
				db.session.add(new_enrollment)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Sucessfully commited')
			db.session.commit()
		
		return redirect('/')


@app.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def update(student_id):
	specific_student = Student.query.filter_by(student_id=student_id).first()
	specific_course_ids = [c.course_id for c in specific_student.enrollment]

	if request.method == 'GET':
		return render_template(
			'update.jinja2.html',
			specific_student=specific_student,
			specific_course_ids=specific_course_ids
			)
	
	if request.method == 'POST':
		# getting form data
		updated_first_name = request.form.get('f_name')
		updated_last_name = request.form.get('l_name')
		updated_course_ids = [int(c[-1]) for c in request.form.getlist('courses')]

		# updating database
		try:
			# update student record
			specific_student.first_name = updated_first_name
			specific_student.last_name = updated_last_name
			
			# update enrollment records
			for course_id in range(1, 5):
				# to add a course
				if course_id in updated_course_ids and course_id not in specific_course_ids:
					new_enrollment = Enrollments(estudent_id=student_id, ecourse_id=course_id)
					db.session.add(new_enrollment)
				# to remove a course
				if course_id in specific_course_ids and course_id not in updated_course_ids:
					specific_enrollment = Enrollments.query.filter_by(estudent_id=student_id, ecourse_id=course_id).first()
					db.session.delete(specific_enrollment)
		except Exception as e:
			print(e)
			db.session.rollback()
			raise
		else:
			# print('Successfully commited')
			db.session.commit()

		return redirect('/')


@app.route('/student/<int:student_id>/delete')
def delete(student_id):
	try:
		specific_student = Student.query.filter_by(student_id=student_id).first()
		db.session.delete(specific_student)

		for specific_enrollment in Enrollments.query.filter_by(estudent_id=student_id).all():
			db.seesion.delete(specific_enrollment)
	except Exception as e:
		print(e)
		db.session.rollback()
		raise
	else:
		print('Successfully commited')
		db.session.commit()

	return redirect('/')

@app.route('/student/<int:student_id>')
def summary(student_id):
	specific_student = Student.query.filter_by(student_id=student_id).first()
	specific_courses = specific_student.enrollment
	return render_template(
		'summary.jinja2.html',
		specific_student=specific_student,
		specific_courses=specific_courses
		)


if __name__ == '__main__':
	app.run(debug=True)

