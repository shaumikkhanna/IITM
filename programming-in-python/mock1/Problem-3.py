def consolidate(students):
	consol = dict()

	for student in students:
		for subject in student:
			try:
				consol[subject] += 1
			except KeyError:
				consol[subject] = 1

	return consol


def popular(consol):
	most_popular_course = None
	max_students = 0

	for subject, popularity in consol.items():
		if popularity > max_students:
			most_popular_course = subject
			max_students = popularity

	return most_popular_course

