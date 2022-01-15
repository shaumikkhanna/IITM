import matplotlib.pyplot as plt
from jinja2 import Template
import pandas as pd
import sys


data = pd.read_csv('data.csv', dtype=int)
data.columns = ['student_id', 'course_id', 'marks']


def student_information(student_id):
	jinja_student_information = """

	<!DOCTYPE html>
	<html>
	<head>
		<title>Student Data</title>
	</head>
	<body>
		<h1>Student Details</h1>
		<table border="1px solid black">
			<tr>
				<th>Student Id</th>
				<th>Course Id</th>
				<th>Marks</th>
			</tr>
			{% for _, row in table_data.iterrows() %}
			<tr>
				<td>{{ row[0] }}</td>
				<td>{{ row[1] }}</td>
				<td>{{ row[2] }}</td>
			</tr>
			{% endfor %}
			<tr>
				<td colspan="2" align="center">Total Marks</td>
				<td>{{ table_data['marks'].sum() }}</td>
			</tr>
		</table>
	</body>
	</html>

	"""

	table_data = data[data['student_id'] == student_id]
	if table_data.empty:
		return something_went_wrong()

	t = Template(jinja_student_information)

	return t.render(table_data=table_data)


def make_histogram(values):
	plt.hist(values, edgecolor='black')
	plt.xlabel('Marks')
	plt.ylabel('Frequency')
	plt.tight_layout()
	plt.savefig('histogram.png')


def course_information(course_id):
	jinja_course_information = """
	
	<!DOCTYPE html>
	<html>
	<head>
		<title>Course Data</title>
	</head>
	<body>
		<h1>Course Details</h1>
		<table border="1px solid black">
			<tr>
				<th>Average Marks</th>
				<th>Maximum Marks</th>
			</tr>
			<tr>
				<td>{{ table_data['marks'].mean() }}</td>
				<td>{{ table_data['marks'].max() }}</td>
			</tr>
		</table>
		<br>
		<img src="histogram.png">
	</body>
	</html>

	"""

	table_data = data[data['course_id'] == course_id]
	if table_data.empty:
		return something_went_wrong()

	make_histogram(table_data['marks'])

	t = Template(jinja_course_information)

	return t.render(table_data=table_data)


def something_went_wrong():
	return """

	<!DOCTYPE html>
	<html>
	<head>
		<title>
			Something went wrong.
		</title>
	</head>
	<body>
		<h1>
			Wrong Inputs
		</h1>
		Something went wrong.
	</body>
	</html>

	"""


def main():
	option = sys.argv[1]
	value_id = int(sys.argv[2])
	
	if option == '-s':
		content = student_information(value_id)
	elif option == '-c':
		content = course_information(value_id)
	else:
		content = something_went_wrong()

	with open('output.html', 'w') as f:
		f.write(content)


if __name__ == '__main__':
	main()

