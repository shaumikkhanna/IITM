from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)


# Link database to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy()
db.init_app(app)

# Create Api object
api = Api(app)


app.app_context().push()


# Import all controllers
from controllers import *

# Add all restfulAPI controllers
from api import UserAPI
api.add_resource(UserAPI, 
	"/api/course/{course_id}", 
	"/api/course",
	"/api/student/{student_id}",
	"/api/student/{student_id}/course",
	"/api/student/{student_id}/course/{course_id}"
	)


if __name__ == '__main__':
	app.run(debug=True)

