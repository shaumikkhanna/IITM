
x, y, z = [], [], []
with open('fixedWidth.txt', 'r') as f:
    f.readline()
    for line in f.readlines():
        x0, y0, z0 = line.strip().split()
        x.append(float(x0))
        y.append(float(y0))
        z.append(float(z0))

avg = lambda x: f'{sum(x) / len(x):.2f}'
print(f'{avg(x)} {avg(y)} {avg(z)}')
