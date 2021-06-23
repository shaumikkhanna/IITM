name1 = input()
date1 = input()
name2 = input()
date2 = input()


from datetime import datetime


date1 = datetime.strptime(date1, '%d-%m-%Y')
date2 = datetime.strptime(date2, '%d-%m-%Y')

if date1 == date2:
	print(sorted([name1, name2])[0])
else:
	print(name1 if date1 > date2 else name2)
