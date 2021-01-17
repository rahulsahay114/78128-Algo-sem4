import random as r
import math
import matplotlib.pyplot as plt
import csv 

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
                noOfComp += 1
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

def plot(lstBest, lstAvg, lstWorst):
    
    xAvg = [] 
    yAvg = [] 

    xBest = [] 
    yBest = [] 

    xWorst = [] 
    yWorst = [] 

    yLog = []

    lstAvg.sort() #sorting by size of inputs.
    lstBest.sort() #sorting by size of inputs.
    lstWorst.sort() #sorting by size of inputs.
    
    for i in range(len(lstAvg)):
        xAvg.append(lstAvg[i][0]) #'size of inputs' extracted.
        yAvg.append(lstAvg[i][1])

    for i in range(len(lstBest)):
        xBest.append(lstBest[i][0]) #'size of inputs' extracted.
        yBest.append(lstBest[i][1])

    for i in range(len(lstWorst)):
        xWorst.append(lstWorst[i][0]) #'size of inputs' extracted.
        yWorst.append(lstWorst[i][1])

    for i in range(len(xAvg)):
        yLog.append(xAvg[i]*math.log(xAvg[i],2))

    plt.plot(xAvg,yAvg)
    plt.plot(xBest,yBest, 'r--')
    plt.plot(xWorst,yWorst, 'y')
    plt.plot(xAvg, yLog, 'g.-')
    plt.legend(['Average Case', 'Best Case', 'Worst Case', 'nlogn'])
    plt.xlabel('Size of Input')
    plt.ylabel('Number of comparisions')
    plt.grid(True)
    plt.show()

def avg_case():
    
    ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

    noOfRuns = r.randint(10, 100) #deciding the total number of runs to be made

    while(noOfRuns > 0):
        
        x = 0
        noOfInp = r.randint(0, 600) #input size
        a = [int(i*r.random()) for i in range(noOfInp)]
        x = mergeSort(a) #comparisions

        ListOfInpSizeAndComps.append((noOfInp, x)) #list of tuples.
        
        noOfRuns -= 1

    #print('List of Comparisons made in each run: \n{}'.format(tot))
    #print('\nTotal Runs: {}'.format(len(tot)))

    return ListOfInpSizeAndComps

def worst_case():
    
    ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

    noOfRuns = r.randint(10, 100) #deciding the total number of runs to be made

    while(noOfRuns > 0):
        
        x = 0
        noOfInp = r.randint(0, 600) #input size
        a = [int(i*r.random()) for i in range(noOfInp)]
        a.sort(reverse = True)
        x = mergeSort(a) #comparisions

        ListOfInpSizeAndComps.append((noOfInp, x)) #list of tuples.
        
        noOfRuns -= 1

    return ListOfInpSizeAndComps

def best_case():

    ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

    noOfRuns = r.randint(10, 100) #deciding the total number of runs to be made

    while(noOfRuns > 0):
        
        x = 0
        noOfInp = r.randint(0, 600) #input size
        a = [int(i*r.random()) for i in range(noOfInp)]
        a.sort()
        x = mergeSort(a) #comparisions

        ListOfInpSizeAndComps.append((noOfInp, x)) #list of tuples.
        
        noOfRuns -= 1

    return ListOfInpSizeAndComps

def main():

    lstAvg = avg_case()
    lstBest = best_case()
    lstWorst = worst_case()

    plot(lstBest, lstAvg, lstWorst) 

    lstAvg.insert(0, 'AVG(InpSize,Cmprsns)')
    lstBest.insert(0, 'BEST(InpSize,Cmprsns)')
    lstWorst.insert(0, 'WORST(InpSize,Cmprsns)')

    allLists = [lstAvg, lstWorst, lstBest]

    with open('data_mergesort.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(allLists)



main()

