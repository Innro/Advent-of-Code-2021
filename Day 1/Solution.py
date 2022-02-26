measurements = list()

with open('Day 1\input.txt') as file:
    measurements = file.read().splitlines()

measurement_increase_counter = 0

for i in range(1,len(measurements)):
    if int(measurements[i]) > int(measurements[i-1]):
        measurement_increase_counter += 1

print(measurement_increase_counter)
