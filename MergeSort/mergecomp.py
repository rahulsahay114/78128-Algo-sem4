import random as r
import math
import matplotlib.pyplot as plt
tot = [] #list of number of comparisons made in different runs of insertion sort.
inps = []

ListOfInpSizeAndComps = []

def mergeSort(arr):
    
    noOfComp = 0

    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                noOfComp += 1
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return noOfComp

def plot(lst):
    
    x = [] 
    y = [] 
    yLog = []

    lst.sort() #sorting by size of inputs.
    
    for i in range(len(lst)):
        x.append(lst[i][0]) #'size of inputs' extracted.
        y.append(lst[i][1])


    plt.plot(x,y)
    
    plt.legend(['Average', 'nlogn'])
    plt.xlabel('Size of Input')
    plt.ylabel('Number of comparisions')
    plt.grid(True)
    plt.show()

def main():

    noOfRuns = r.randint(200, 300) #deciding the total number of runs to be made

    while(noOfRuns > 0):
        
        x = 0
        noOfInp = r.randint(100, 2000) #input size
        a = [int(i*r.random()) for i in range(noOfInp)]
        x = mergeSort(a) #comparisions

        ListOfInpSizeAndComps.append((noOfInp, x))
        
        noOfRuns -= 1

    #print('ListOfInpSizeAndComps: \n{}'.format(ListOfInpSizeAndComps))
    #print(a)

    plot(ListOfInpSizeAndComps)

main()