def getFreq(arr):
	frequency = {}

	# iterating over the list
	for item in arr:
		# checking the element in dictionary
		if item in frequency:
			# incrementing the count
			frequency[item] += 1
		else:
			# initializing the count
			frequency[item] = 1

	return(frequency)

def main():
	print("This is a function for testing, this file is a utils file only.")
	print(getFreq(["a", "b", "c", "a", "b", "c", "a", "b", "c"]))

if __name__ == '__main__':
	main()