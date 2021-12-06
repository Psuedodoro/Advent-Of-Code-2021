# Day 2, part 1 of Advent of Code

# Open the file and put each line in a list
with open('input.txt', 'r') as f:
    data = f.read().split("\n")

# Define a horizontal and vertical position variable
horizontal = 0
depth = 0

for i in range(len(data)):
    splitvalues = data[i].split(" ")

    match splitvalues[0]:
        case "forward":
            horizontal += int(splitvalues[1])
        case "down":
            depth += int(splitvalues[1])
        case "up":
            depth -= int(splitvalues[1])

print('Horizontal Value: ' + str(horizontal))
print('Depth Value: ' + str(depth))
print('Horizontal x Depth:', (horizontal * depth))
