def topMentors(scores, subject):
	best_mentor, best_mentor_max, best_mentor_list = None, 0, []
	for mentor in scores:
		list_of_mentees = []
		for mentee in scores:
			if 10 <= mentor[subject] - mentee[subject] <= 20:
				list_of_mentees.append(mentee['SeqNo'])

		no_of_mentees = len(list_of_mentees)
		if no_of_mentees > best_mentor_max:
			best_mentor = mentor['SeqNo']
			best_mentor_max = no_of_mentees
			best_mentor_list = list_of_mentees.copy()

	return {best_mentor:best_mentor_list}

