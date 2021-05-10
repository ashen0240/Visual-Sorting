import random

#Create the array
numnums = 100
speed = 1 #big nums slower
sortingMethod = "Bubble Sort"

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
    #average and worst complexity of O(n^2) but a best case of O(n)
    #error that copies two to the same

    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
            yield array
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
                
            yield array

        array[i], array[index] = array[index], array[i]
        yield array



def bubbleSort(array):
    #works by picking up the largest number and swaping it to the back, 
    #comparing one by one which is greater
    #average and worst complexity of O(n^2) but a best case of O(n)

    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
            yield array



def mergeSort(array):
    #I UNDERSTAND THE THEORY WELL, NEED TO LOOK OVER IMPLEMENTATION MORE
    #beaks the array down into pairs, sorting each pairs
    #combines pairs and sorts
    #repeat the combination unitl you have the whole array
    #always O(nlog(n)) complexity

    mergeSortHelper(array, 0, len(array)-1)

def mergeSortHelper(arr,l,r):
    if l < r:
  
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l+(r-1))//2
  
        # Sort first and second halves
        yield from mergeSortHelper(arr, l, m)
        yield from mergeSortHelper(arr, m+1, r)
        yield from merge(arr, l, m, r)
        yield array
    return

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
  
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
  
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
  
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
  
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
  
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    yield array


def heapSort(array):
    #NEED TO UNDERSTAND MORE
    #turns the array into a heap
    #sorts the heap into a max heap (every child is less than its parent)
    #removes the first node (largest num), and put the smallest node in its place
    #sort back into max heap and replace
    #always O(nlog(n)) complexity
    n = len(array)
 
    #Builds the maxHeap
    for i in range(n//2 - 1, -1, -1):
        yield from heapify(array, n, i)
 
    #One by one extracts the parent node
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        yield from heapify(array, i, 0)

def heapify(array, n, i):
    #recursivly creates the maxHeap
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and array[largest] < array[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and array[largest] < array[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swap
        yield  array
 
        # Heapify the root.
        heapify(array, n, largest)

 

def quickSort(array):
    #YIELD NOT WORKING
    #for ease of calling
    #worst case o(n^2) but average and best of O(nlog(n))
    quickSortHelper(array, 0, len(array)-1)

def quickSortHelper(array, start, end):
    #recursivly applies the partition function to sort the array 
    if start >= end:
        return

    p = partition(array, start, end)
    yield from quickSortHelper(array, start, p-1)
    yield from quickSortHelper(array, p+1, end)
    yield array
    
def partition(array, start, end):
    #another quickSort Helper function
    #reorders the array around the partition value so that all elements 
    #less than the pivot come before the pivot
    #and all elements with values greater than the pivot come after it
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            yield array
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


"""

mergeSort(array)

for i in range (0, len(array)):
    print(array[i])
"""

import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == "__main__":
    # Get user input to determine range of integers (1 to N) and desired
    # sorting method (algorithm).

    # Build and randomly shuffle list of integers.
    random.seed(time.time())

    # Get appropriate generator to supply to matplotlib FuncAnimation method.
    title = sortingMethod
    if sortingMethod == "Bubble Sort":
        generator = bubbleSort(array)
    elif sortingMethod == "Insertion Sort":
        generator = insertionSort(array)
    elif sortingMethod == "Merge Sort":
        generator = mergeSort(array)
    elif sortingMethod == "Quick Sort":
        generator = quickSort(array)
    elif sortingMethod == "Heap Sort":
        generator = heapSort(array)
    else:
        generator = selectionSort(array)

    # Initialize figure and axis.
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
    # list of rectangles (with each bar in the bar plot corresponding
    # to one rectangle), which we store in bar_rects.
    bar_rects = ax.bar(range(len(array)), array, align="edge")

    # Set axis limits. Set y axis upper limit high enough that the tops of
    # the bars won't overlap with the text label.
    ax.set_xlim(0, numnums)
    ax.set_ylim(0, int(1.07 * numnums))

    # Place a text label in the upper-left corner of the plot to display
    # number of operations performed by the sorting algorithm (each "yield"
    # is treated as 1 operation).
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
    # To track the number of operations, i.e., iterations through which the
    # animation has gone, define a variable "iteration". This variable will
    # be passed to update_fig() to update the text label, and will also be
    # incremented in update_fig(). For this increment to be reflected outside
    # the function, we make "iteration" a list of 1 element, since lists (and
    # other mutable objects) are passed by reference (but an integer would be
    # passed by value).
    # NOTE: Alternatively, iteration could be re-declared within update_fig()
    # with the "global" keyword (or "nonlocal" keyword).
    iteration = [0]
    def update_fig(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=speed,
        repeat=False)
    plt.show()