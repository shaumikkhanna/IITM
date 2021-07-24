input_ = input()

from string import ascii_uppercase as au

total = 0
for place, letter in enumerate(input_[::-1]):
	total += 26**place * (au.find(letter) + 1)

print(total)
