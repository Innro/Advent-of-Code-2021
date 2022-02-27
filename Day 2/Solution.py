instructions = list()

with open('Day 2\input.txt') as file:
    instructions = file.read().splitlines()

horizontal_position = 0
depth = 0

for i in instructions:
    if i.split()[0] == "forward":
        horizontal_position += int(i.split()[1])
    if i.split()[0] == "down":
        depth += int(i.split()[1])
    if i.split()[0] == "up":
        depth -= int(i.split()[1])

print(horizontal_position * depth)
