#

def trending(subject_topics):
	all_subjects = []
	for subject in subject_topics:
		all_subjects += subject
	
	occurances = dict()
	for subject in all_subjects:
		try:
			occurances[subject] += 1
		except KeyError:
			occurances[subject] = 1
	
	min_ = min(occurances.values())
	max_ = max(occurances.values())

	min_count = sum(freq == min_ for freq in occurances.values())
	max_count = sum(freq == max_ for freq in occurances.values())

	return max_count, min_count

