def line_to_data(line):
    print(line)
    return 0


# read data:
with open('dwz-liste.txt') as ifh:
    data = [line_to_data(line) for line in ifh.readlines()]

print('done doing nothing')