from sys import argv

f_nums = argv[1]

with open(f_nums) as f:
    massiv = [int(i) for i in f.read().split()]
    average = round(sum(massiv)/len(massiv))
    count = 0

    for i in massiv:
        while i != average:
            if i < average:
                i += 1
            elif i > average:
                i -= 1
            count += 1

print(count)