
scores = dict()
subjects = ['Physics', 'Math', 'Chemistry', 'Computer']

with open('responsesheet.txt', 'r') as f:
	student_name = f.readline().strip()
	for subject in subjects:
		f.readline()
		score = 0
		for _ in range(25):
			_, correct_answer, student_answer = f.readline().strip().split('-')
			if student_answer == 'NA':
				continue
			else:
				score += 4 if student_answer == correct_answer else -1
		scores[subject] = score

print(student_name)
for subject in subjects:
	print(f'{subject} = {scores[subject]}/100')
