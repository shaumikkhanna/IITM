def parse(word):
	for p in r':;,.!':
		word = word.replace(p, '')
	return word.lower()

def freqWords(words):
	out = dict()
	words = list(map(parse, words))

	for word in set(words):
		try:
			out[words.count(word)].append(word)
		except KeyError:
			out[words.count(word)] = [word]

	return out
