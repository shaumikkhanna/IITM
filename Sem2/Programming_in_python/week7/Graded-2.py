TEST_CASE = input()

no_of_rows = int(input())
_, *keys = input().split(',')

students = dict()
for _ in range(no_of_rows):
	id_, *row = map(int, input().split(','))
	students[id_] = dict(zip(keys, row))