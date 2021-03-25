def swapValues(theList: list, firstIndex: int) -> None:
	firstValue = theList[firstIndex]  # store first value
	theList[firstIndex] = theList[firstIndex + 1]  # replace first value with second value
	theList[firstIndex + 1] = firstValue  # replace second value with stored first value


def bubbleSort(theList: list) -> int:
	listLen = len(theList)
	swappedInThisPass = False
	swaps = 0

	for passNum in range(listLen - 1):

		for i in range(listLen - passNum - 1):
			if theList[i] > theList[i + 1]:
				swapValues(theList, i)
				swaps += 1
				# print(f"swap #{swaps}: {theList}")
				swappedInThisPass = True

		if not swappedInThisPass:
			break

	return swaps


# test bubble sort with different worse-case lists
ns = range(4, 100)
print("n\tswaps")

for n in ns:
	thisList = list(range(n, 0, -1))  # list of n down to 1 step 1 (as the 0 is exclusive)
	swaps = bubbleSort(thisList)
	print(f"{n}\t{swaps}")
