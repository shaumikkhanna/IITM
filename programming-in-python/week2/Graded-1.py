a = int(input())
b = int(input())
c = int(input())


sides = [a, b, c]
hypotenuse = max(sides)
sides.remove(hypotenuse)


print('YES' if hypotenuse**2 == sides[0]**2 + sides[1]**2 else 'NO')