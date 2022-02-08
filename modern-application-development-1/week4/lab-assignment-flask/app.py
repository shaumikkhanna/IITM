from flask import Flask, render_template, request, url_for
import csv
import matplotlib.pyplot as plt


app = Flask(__name__)


with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	reader.__next__()
	data = [{
		'student_id': int(row[0]),
		'course_id': int(row[1]),
		'marks': int(row[2])
		} for row in reader]


def mean(lst):
	return sum(lst) / len(lst)


def make_histogram(xs):
	plt.hist(xs, edgecolor='black', color='red')
	plt.xlabel('Marks')
	plt.ylabel('Frequency')

	plt.tight_layout()
	plt.savefig('static/histogram.png')


@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return render_template('index.html')
	
	if request.method == 'POST':
		# Process inputs
		radio_student = bool(request.form.get('student_id'))
		radio_course = bool(request.form.get('course_id'))
		id_value = request.form.get('id_value')

		# Invalid Inputs
		if (not radio_student ^ radio_course) or (not id_value):
			return render_template('error.html')

		# For student information page
		if radio_student:
			table_data = [row for row in data if row['student_id'] == int(id_value)]
			if not table_data:
				return render_template('error.html')
			
			return render_template(
				'student.html', 
				table_data=table_data,
				total_marks=sum(row['marks'] for row in table_data)
				)
		
		# For course information page
		if radio_course:
			table_data = [row for row in data if row['course_id'] == int(id_value)]
			if not table_data:
				return render_template('error.html')

			marks_data = [row['marks'] for row in table_data]
			make_histogram(marks_data)

			return render_template(
				'course.html',
				avg_marks=mean(marks_data),
				max_marks=max(marks_data)
				)


if __name__ == '__main__':
	app.run(debug=True)

