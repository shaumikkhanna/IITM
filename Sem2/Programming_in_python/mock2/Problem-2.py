eng_dict = dict()
for word in words:
	word = word.lower()
	starting_letter = word[0]
	try:
		eng_dict[starting_letter].add(word)
	except KeyError:
		eng_dict[starting_letter] = set([word])
