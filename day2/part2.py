# Day 2, part 2 of Advent of Code

# Open the file and put each line in a list
with open('input.txt', 'r') as f:
	data = f.read().split("\n")

# Define horizontal, depth and aim variables
horizontal = 0
depth = 0
aim = 0

for i in range(len(data)):
	splitvalues = data[i].split(" ")
	keyword = splitvalues[0]
	x = splitvalues[1]

	match keyword:
		case "forward":
			horizontal += int(x)
			depth += aim * int(x)
		case "down":
			aim += int(x)
		case "up":
			aim -= int(x)

print('Horizontal Value: ' + str(horizontal))
print('Depth Value: ' + str(depth))
print('Horizontal x Depth:', (horizontal * depth))
