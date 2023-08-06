from flask import Flask 
from database import db


app = Flask(__name__)


# Link database to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)


# Import all controllers
from controllers import *

if __name__ == '__main__':
	app.run(debug=True)

