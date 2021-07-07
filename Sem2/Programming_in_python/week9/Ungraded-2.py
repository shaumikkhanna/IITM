
out = dict((class_, 0) for class_ in 'ABCDE')

def to_class(ip):
	first, *_ = ip.split('.')
	first = int(first, base=2)
	
	if first < 128:
		return 'A'
	if first < 192:
		return 'B'
	if first < 224:
		return 'C'
	if first < 240:
		return 'D'
	return 'E'

with open('ipaddress.txt', 'r') as f:
	for line in f.readlines():
		line = line.strip()
		if line == 'END':
			break
		else:
			out[to_class(line)] += 1

for class_ in 'ABCDE':
	print(f'{class_} = {out[class_]}')
