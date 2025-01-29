s = input()
lines = s.split('\n')
max_length = max(len(line) for line in lines)
lines = [line.ljust(max_length) for line in lines]
rotated = [''.join(line[i] for line in reversed(lines)) for i in range(max_length)]

for row in rotated:
    print(row)
