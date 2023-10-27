from sys import argv

file_circle = argv[1]
file_points = argv[2]

with open(file_circle) as fi, open(file_points) as fo:
    x, y = fi.readline().split()
    x, y = float(x), float(y)
    radius = float(fi.readline())

    for line in fo.readlines():
        x_point, y_point = line.strip().split()
        x_point, y_point = float(x_point), float(y_point)
        if (x_point - x)**2 + (y_point - y)**2 > radius**2: print('2 - точка снаружи')
        elif (x_point - x)**2 + (y_point - y)**2 < radius**2: print('1 - точка внутри')
        elif (x_point - x)**2 + (y_point - y)**2 == radius**2: print('0 - точка лежит на окружности')