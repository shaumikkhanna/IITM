from flask import render_template, request, redirect, url_for
from models import *
from app import app
from hashlib import sha1
import datetime
import matplotlib.pyplot as plt


# CONTROLLERS
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		hash_ = None
		for l in Login.query.all():
			if l.username == username:
				hash_ = l.password
				break
		print(hash_)
		if hash_ is None:
			return redirect('/signup')
		else:
			if sha1(password.encode()).hexdigest() == hash_:
				return redirect(f'/dashboard/{username}')
			else:
				return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		password2 = request.form.get('password2')

		if password != password2:
			return redirect('/signup')

		try:
			new_login = Login(username=username, password=sha1(password.encode()).hexdigest())
			db.session.add(new_login)
		except Exception as e:
			print(e)
			db.session.rollback()
			print('Something went wrong')
		else:
			print('Sucessfully commited')
			db.session.commit()

		return redirect('/')

@app.route('/dashboard/<string:username>', methods=['GET'])
def dashboard(username):
	trackers = list(
			Tracker.query.filter_by(username=username).all()
		)
	return render_template(
			'dashboard.html', 
			username=username, 
			trackers=trackers
		)

@app.route('/tracker/create/<string:username>', methods=['GET', 'POST'])
def createtracker(username):
	if request.method == 'GET':
		return render_template(
				'createtracker.html',
				username=username
			)
	if request.method == 'POST':
		tracker_name = request.form.get('tracker_name')
		tracker_type = request.form.get('tracker_type')
		categories = request.form.get('categories')
		tracker_description = request.form.get('tracker_description')

		if tracker_type is None:
			return redirect(f'/tracker/create/{username}')

		try:
			if tracker_type == 'categorical':
				new_tracker = Tracker(
					tracker_name=tracker_name, 
					tracker_type=tracker_type, 
					username=username,
					categories=categories,
					tracker_description=tracker_description
				)
			else:
				new_tracker = Tracker(
					tracker_name=tracker_name, 
					tracker_type=tracker_type, 
					username=username
				)
			db.session.add(new_tracker)
		except Exception as e:
			print(e)
			db.session.rollback()
			print('Something went wrong')
		else:
			db.session.commit()
			print('Commited Sucessfully')

		return redirect(f'/dashboard/{username}')

@app.route('/tracker/edit/<string:username>/<int:tracker_id>', methods=['GET', 'POST'])
def edittracker(username, tracker_id):
	tracker = Tracker.query.filter_by(tracker_id=tracker_id).first()
	if request.method == 'GET':
		return render_template(
				'edittracker.html',
				username=username,
				tracker=tracker
			)
	if request.method == 'POST':
		tracker_name = request.form.get('tracker_name')
		tracker_description = request.form.get('tracker_description')

		try:
			tracker.tracker_name = tracker_name
			tracker.tracker_description = tracker_description
			db.session.add(tracker)
		except Exception as e:
			print(e)
			db.session.rollback()
			print('Something went wrong')
		else:
			db.session.commit()
			print('Commited Sucessfully')

		return redirect(f'/dashboard/{username}')

@app.route('/tracker/delete/<string:username>/<int:tracker_id>')
def deletetracker(username, tracker_id):
	try:
		for log in Tracker_log.query.filter_by(tracker_id=tracker_id).all():
			db.session.delete(log)
		db.session.delete(Tracker.query.filter_by(tracker_id=tracker_id).first())
	except Exception as e:
		print(e)
		db.session.rollback()
		print('Something went wrong')
	else:
		db.session.commit()
		print('Committed Sucessfully')

	return redirect(f'/dashboard/{username}')

@app.route('/log/create/<string:username>/<int:tracker_id>', methods=['GET', 'POST'])
def addlog(username, tracker_id):
	tracker = Tracker.query.filter_by(tracker_id=tracker_id).first()
	if request.method == 'GET':
		timestamp_now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
		return render_template(
				'addlog.html',
				tracker=tracker,
				timestamp_now=timestamp_now,
				username=username
			)
	if request.method == 'POST':
		timestamp = request.form.get('timestamp')
		timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M")

		value = request.form.get('value')
		if value is None:
			return redirect(f'log/create/{username}/{tracker_id}')

		message = request.form.get('message')

		try:
			new_tracker_log = Tracker_log(
					tracker_id=tracker_id,
					timestamp=timestamp,
					value=value,
					message=message
				)
			db.session.add(new_tracker_log)
		except Exception as e:
			print(e)
			db.session.rollback()
			print('Something went wrong')
		else:
			db.session.commit()
			print('Committed Sucessfully')

		return redirect(f'/dashboard/{username}/{tracker_id}')

@app.route('/log/edit/<string:username>/<int:tracker_id>/<int:log_id>', methods=['GET', 'POST'])
def editlog(username, tracker_id, log_id):
	log = Tracker_log.query.filter_by(log_id=log_id).first()
	tracker = Tracker.query.filter_by(tracker_id=tracker_id).first()
	timestamp_default = log.timestamp.strftime("%Y-%m-%dT%H:%M")

	if request.method == 'GET':
		return render_template(
				'editlog.html',
				username=username,
				log=log,
				tracker=tracker,
				timestamp_default=timestamp_default
			)

	if request.method == 'POST':
		timestamp = datetime.datetime.strptime(request.form.get('timestamp'), "%Y-%m-%dT%H:%M")
		value = request.form.get('value')
		if value is None:
			return redirect(f'/log/create/{username}/{tracker_id}/{log_id}')
		message = request.form.get('message')

		try:
			log.timestamp = timestamp
			log.message = message
			log.value = value
			db.session.add(log)
		except Exception as e:
			print(e)
			db.session.rollback()
			print('Something went wrong')
		else:
			db.session.commit()
			print('Committed Sucessfully')

		return redirect(f'/dashboard/{username}/{tracker_id}')

@app.route('/log/delete/<string:username>/<int:tracker_id>/<int:log_id>')
def deletelog(username, tracker_id, log_id):
	try:
		db.session.delete(Tracker_log.query.filter_by(log_id=log_id).first())
	except Exception as e:
		print(e)
		db.session.rollback()
		print('Something went wrong')
	else:
		db.session.commit()
		print('Committed Sucessfully')

	return redirect(f'/dashboard/{username}/{tracker_id}')

@app.route('/dashboard/<string:username>/<int:tracker_id>')
def display_tracker(username, tracker_id):
	tracker = Tracker.query.filter_by(tracker_id=tracker_id).first()
	tracker_logs = Tracker_log.query.filter_by(tracker_id=tracker_id).order_by(Tracker_log.timestamp.desc()).all()
	
	x, y = [], []

	if tracker.tracker_type == 'numeric':
		for log in tracker_logs:
			x.append(log.timestamp)
			y.append(float(log.value))
		
		plt.style.use('ggplot')
		plt.plot(x, y)
		plt.xlabel('Time')
		plt.ylabel('Value')
		plt.tight_layout()
		plt.savefig('static/graph.png')

	elif tracker.tracker_type == 'boolean':
		for log in tracker_logs:
			y.append(log.value == 'yes')
		ratio = sum(y) / len(y)
		plt.pie([ratio, 1 - ratio], labels=['Yes', 'No'])
		plt.legend()
		

	elif tracker.tracker_type == 'categorical':
		for log in tracker_logs:
			y.append(log.value)
		plt.hist(y, edgecolor='black')
		plt.xlabel('Categories')
		plt.ylabel('Value')


	plt.tight_layout()
	plt.savefig('static/graph.png')
	plt.clf()
	plt.cla()

	return render_template(
			'trackerpage.html',
			tracker=tracker,
			username=username,
			tracker_logs=tracker_logs
		)

