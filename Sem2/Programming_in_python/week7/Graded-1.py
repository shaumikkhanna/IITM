from string import digits

to_word = dict(zip(digits, [
	'zero', 'one', 'two', 'three', 'four', 
	'five', 'six', 'seven', 'eight', 'nine'
	]))

out = [to_word[digit] for digit in input()]
out.append(out[0] + ''.join(word.capitalize() for word in out[1:]))

print('\n'.join(out))
