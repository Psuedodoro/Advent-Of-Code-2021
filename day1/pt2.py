from pt1 import get_increases

with open('input.txt', 'r') as f:
    numbers = f.read().split("\n")
    numbers = list(map(int, numbers))

sums = []

for i in range(len(numbers) - 2):
    nums = numbers[i:i+3]
    sums.append(sum(nums))

get_increases(sums)
