a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

f = lambda x, y: not ((x + y) % 2)

truth = f(a, b) and f(b, c) and f(c, d) and f(d, e) and f(e, a)
print('YES' if truth else 'NO')