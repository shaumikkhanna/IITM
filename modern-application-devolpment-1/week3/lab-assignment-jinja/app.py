import sys
import csv
import matplotlib.pyplot as plt
from jinja2 import Template


with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	reader.__next__()

	data = [{
		'student_id': int(row[0]),
		'course_id': int(row[1]),
		'marks': int(row[2])
	} for row in reader]


def make_histogram(values):
	plt.hist(values, edgecolor='black')
	plt.xlabel('Marks')
	plt.ylabel('Frequency')
	
	plt.tight_layout()
	plt.savefig('histogram.png')


def mean(lst):
	return sum(lst) / len(lst)


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
			{% for row in table_data %}
			<tr>
				<td>{{ row['student_id'] }}</td>
				<td>{{ row['course_id'] }}</td>
				<td>{{ row['marks'] }}</td>
			</tr>
			{% endfor %}
			<tr>
				<td colspan="2" align="center">Total Marks</td>
				<td>{{ total_marks }}</td>
			</tr>
		</table>
	</body>
	</html>

	"""

	table_data = [row for row in data if row['student_id'] == student_id]
	if not table_data:
		return something_went_wrong()

	t = Template(jinja_student_information)

	return t.render(
		table_data=table_data, 
		total_marks=sum(row['marks'] for row in table_data)
		)


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
				<td>{{ avg_marks }}</td>
				<td>{{ max_marks }}</td>
			</tr>
		</table>
		<br>
		<img src="histogram.png">
	</body>
	</html>

	"""

	table_data = [row for row in data if row['course_id'] == course_id]
	if not table_data:
		return something_went_wrong()

	marks_array = [row['marks'] for row in table_data]

	make_histogram(marks_array)
	t = Template(jinja_course_information)

	return t.render(
		table_data=table_data, 
		avg_marks=mean(marks_array), 
		max_marks=max(marks_array)
		)


def something_went_wrong():
	return """

	<!DOCTYPE html>
	<html>
	<head>
		<title>
			Something Went Wrong
		</title>
	</head>
	<body>
		<h1>
			Wrong Inputs
		</h1>
		Something went wrong
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
