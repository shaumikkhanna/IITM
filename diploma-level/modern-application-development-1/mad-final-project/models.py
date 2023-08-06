from database import db
import datetime


# MODELS
class Login(db.Model):
	__tablename__ = 'login'
	username = db.Column(db.String, primary_key=True)
	password = db.Column(db.String, nullable=False)

class Tracker(db.Model):
	__tablename__ = 'trackers'
	tracker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tracker_name = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False)
	tracker_type = db.Column(db.String, nullable=False)
	categories = db.Column(db.String)
	tracker_description = db.Column(db.String)

	def last_tracked(self):
		most_recent = Tracker_log.query.filter_by(tracker_id=self.tracker_id).order_by(Tracker_log.timestamp.desc()).first()	
		if most_recent is None:
			return 'Never'

		most_recent = most_recent.timestamp
		now = datetime.datetime.now()
		diff = now - most_recent
		second_diff = diff.seconds
		day_diff = diff.days

		# less than a day ago
		if day_diff == 0:
			if second_diff < 10:
				return "Just now"
			if second_diff < 60:
				return str(second_diff) + " seconds ago"
			if second_diff < 120:
				return "A minute ago"
			if second_diff < 3600:
				return str(second_diff // 60) + " minutes ago"
			if second_diff < 7200:
				return "An hour ago"
			if second_diff < 86400:
				return str(second_diff // 3600) + " hours ago"
	
		if day_diff == 1:
			return "Yesterday"
		if day_diff < 7:
			return str(day_diff) + " days ago"
		if day_diff < 31:
			return str(day_diff // 7) + " weeks ago"
		if day_diff < 365:
			return str(day_diff // 30) + " months ago"
		
		return str(day_diff // 365) + " years ago"


class Tracker_log(db.Model):
	__tablename__ = 'tracker_logs'
	log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tracker_id = db.Column(db.Integer, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False)
	value = db.Column(db.String, nullable=False)
	message = db.Column(db.String)







