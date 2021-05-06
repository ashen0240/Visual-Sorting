import random

#Create the array
numnums = 100

array = [n for n in range (1,numnums+1)]
#print (array)
random.shuffle(array)
#print (array)

#Algorithms

def insertionSort(array):
    #works by having a sorted and unsorted half of the array. 
    #It picks up the first number in the unsorted half and works 
    #backwards from the sorted half to see where to slot it in, 
    #shifting the array up as it goes

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
    for i in range(len(array)-1):
        index = i
        for j in range(i+1, len(array)-1):
            if array[j] < array[index]:
                index = j

        array[i], array[index] = array[index], array[i]


def bubbleSort(array):
    #works by picking up the largest number and swaping it to the back, 
    #comparing one by one which is greater
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

selectionSort(array)

for i in range (0, len(array)):
    print(array[i])