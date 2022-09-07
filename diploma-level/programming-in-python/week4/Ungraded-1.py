units = int(input())

if units <= 100:
	cost = 0
elif 100 < units <= 200:
	cost = 5*(units - 100)
elif 200 < units <= 500:
	cost = 500 + 8*(units - 200)
elif units >= 500:
	cost = 2900 + 10*(units - 500)

print(cost)