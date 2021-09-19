
max_sentence, length_of_max_sentence = None, 0
sentence_count = 0
word_freq = dict()

with open('file.txt', 'r') as f:
	while True:
		line = f.readline().strip()
		if not line:
			break

		# Number of sentences yet
		sentence_count += 1

		words = line.split(' ')

		# Update max_sentence if necessary
		number_of_words_in_sentence = len(words)
		if number_of_words_in_sentence > length_of_max_sentence:
			length_of_max_sentence = number_of_words_in_sentence
			max_sentence = line

		# Update word_freq dictionary
		for word in words:
			try:
				word_freq[word] += 1
			except KeyError:
				word_freq[word] = 1

word_count = sum(word_freq.values())
unique = list(word_freq.keys())
