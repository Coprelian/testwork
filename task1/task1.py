from sys import argv

m_len = argv[1]
step = int(argv[2])
result = []
massiv = list(range(1, int(m_len) + 1))

while True:
    result.append(massiv[0])
    for index in range(step - 1):
        massiv.append(massiv.pop(0))
    if massiv[0] == 1: break

print(''.join(str(result)).replace('[','').replace(']','').replace(', ',''))