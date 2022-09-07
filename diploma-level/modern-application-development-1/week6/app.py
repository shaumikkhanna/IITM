from flask import Flask
from flask_restful import Api
from database import db


app = Flask(__name__)


# Link database to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'
db.init_app(app)

# Create Api object
api = Api(app)


app.app_context().push()


# Import all controllers and models
from controllers import *

# Add all restfulAPI controllers
from api_resources import CourseAPI, StudentAPI, EnrollmentsAPI
api.add_resource(CourseAPI, 
	"/api/course/<int:course_id>", 
	"/api/course"
	)
api.add_resource(StudentAPI,
	"/api/student/<int:student_id>", 
	"/api/student"
	)
api.add_resource(EnrollmentsAPI,
	"/api/student/<int:student_id>/course",
	"/api/student/<int:student_id>/course/<int:course_id>",
	)

if __name__ == '__main__':
	app.run(debug=True)

