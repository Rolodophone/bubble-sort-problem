def logDebug(msg: str) -> None:
	print(msg)


def swapValues(theList: list, firstIndex: int) -> None:
	firstValue = theList[firstIndex]  # store first value
	theList[firstIndex] = theList[firstIndex + 1]  # replace first value with second value
	theList[firstIndex + 1] = firstValue  # replace second value with stored first value


def bubbleSort(theList: list) -> None:
	listLen = len(theList)
	swappedInThisPass = False
	swaps = 0

	for passNum in range(listLen - 1):

		for i in range(listLen - passNum - 1):
			if theList[i] > theList[i + 1]:
				swapValues(theList, i)
				swaps += 1
				logDebug(f"swap #{swaps}: {theList}")
				swappedInThisPass = True

		if not swappedInThisPass:
			break


bubbleSort([1, 4, 3, 2])
