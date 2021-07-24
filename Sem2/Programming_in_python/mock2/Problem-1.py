start = int(input())
end = int(input())

A = set(num for num in range(start, end+1) if not num % 3)
B = set(num for num in range(start, end+1) if not num % 5)

o1 = A.union(B)
o2 = A.intersection(B)
o3 = A - B
o4 = B - A 

