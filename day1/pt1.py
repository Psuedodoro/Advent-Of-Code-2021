def get_increases(numbers):
    increasedAmount = 0

    # Loop through the data
    for i in range(len(numbers)):
        number = numbers[i]
        if i != 0 and number > numbers[i - 1]:
            increasedAmount += 1

    print("Increments:", increasedAmount)

def main():
	# Get the numbers
	with open('input.txt', 'r') as f:
		numbers = f.read().split("\n")
		numbers = list(map(int, numbers))
	
	get_increases(numbers)

if __name__ == "__main__":
	main()