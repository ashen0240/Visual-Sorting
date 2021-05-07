import random

#Create the array
numnums = 100

array = [n for n in range (1,numnums+1)]
#print (array)
random.shuffle(array)
#print (array)

#mpld3
#Algorithms

def insertionSort(array):
    #works by having a sorted and unsorted half of the array. 
    #It picks up the first number in the unsorted half and works 
    #backwards from the sorted half to see where to slot it in, 
    #shifting the array up as it goes
    #average and worst complexity of O(n) but a best case of O(n)

    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue



def selectionSort(array):
    #works by having a sorted half and unsorted half of the array
    #takes the smallest number from the unsorted half and shoves it into the sorted half
    #Always O(n^2)

    for i in range(len(array)):
        index = i
        for j in range(i+1, len(array)):
            if array[j] < array[index]:
                index = j

        array[i], array[index] = array[index], array[i]



def bubbleSort(array):
    #works by picking up the largest number and swaping it to the back, 
    #comparing one by one which is greater
    #average and worst complexity of O(n) but a best case of O(n)

    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]



def mergeSort(array):
    return



def heapSort(array):
    return



def quickSort(array):
    #for ease of calling
    #worst case o(n^2) but average and best of O(nlog(n))
    quickSortHelper(array, 0, len(array)-1)

def quickSortHelper(array, start, end):
    #recursivly applies the partition function to sort the array 
    if start >= end:
        return

    p = partition(array, start, end)
    quickSortHelper(array, start, p-1)
    quickSortHelper(array, p+1, end)
    
def partition(array, start, end):
    #another quickSort Helper function
    #reorders the array around the partition value so that all elements 
    #less than the pivot come before the pivot
    #and all elements with values greater than the pivot come after it
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high




quickSort(array)

for i in range (0, len(array)):
    print(array[i])