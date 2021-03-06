# the print statements will make the timings a bit innacurate, but its still mostly fine

'''
EXAMPLE OUTPUT:

Searching for 3262021.
Binary search found 3262021.
Binary search took 22 steps.
Binary search finished in 0.0s.
Normal search found 3262021.
Normal search took 3262021 steps.
Normal search finished in 0.21986651420593262s.
'''

import time, random, sys

LIST_MAX_LENGTH = int(1e7)
LIST_MIN_VALUE = 0
LIST_VALUE_TO_SEARCH_FOR = random.randint(LIST_MIN_VALUE, LIST_MAX_LENGTH)
LIST_OF_NUMBERS = range(LIST_MIN_VALUE, LIST_MIN_VALUE + LIST_MAX_LENGTH)

# binary search
binarySearchTimeStart = time.time()

print('Searching for {}.'.format(LIST_VALUE_TO_SEARCH_FOR))

# desiredValue: the number to search for
# orderedNumberList: the ordered list of numbers to search
# minVal: the lowest index to search (ususally 0)
# maxVal: the highest index to search (ususally len(orderedNumberList))
# returns [index, steps]
def recursivelyBinarySearch(desiredValue, orderedNumberList, minVal, maxVal, fixRecursionLimit = True, steps = 0) -> list:

    defaultRecursionLimit = sys.getrecursionlimit()
    sys.setrecursionlimit(len(orderedNumberList) // 2)

    halfwayValue = ((maxVal - minVal) // 2) + minVal
    
    if (orderedNumberList[halfwayValue] < desiredValue):
        sys.setrecursionlimit(defaultRecursionLimit)
        return recursivelyBinarySearch(desiredValue, orderedNumberList, halfwayValue, maxVal, steps = steps + 1)

    elif (orderedNumberList[halfwayValue] > desiredValue):
        sys.setrecursionlimit(defaultRecursionLimit)
        return recursivelyBinarySearch(desiredValue, orderedNumberList, minVal, halfwayValue, steps = steps + 1)

    else:
        sys.setrecursionlimit(defaultRecursionLimit)
        return [halfwayValue, steps]

binarySearchResults = recursivelyBinarySearch(LIST_VALUE_TO_SEARCH_FOR, LIST_OF_NUMBERS, 0, len(LIST_OF_NUMBERS))

print('Binary search found {}.'.format(LIST_OF_NUMBERS[binarySearchResults[0]]))
print('Binary search took {} steps.'.format(binarySearchResults[1]))

binarySearchTimeEnd = time.time()

print('Binary search finished in {}s.'.format(binarySearchTimeEnd - binarySearchTimeStart))

# normal iterative search
normalSearchTimeStart = time.time()

for i in LIST_OF_NUMBERS:

    if (i == LIST_VALUE_TO_SEARCH_FOR):
        print('Normal search found {}.'.format(LIST_OF_NUMBERS[i]))
        print('Normal search took {} steps.'.format(i))
        break

normalSearchTimeEnd = time.time()

print('Normal search finished in {}s.'.format(normalSearchTimeEnd - normalSearchTimeStart))