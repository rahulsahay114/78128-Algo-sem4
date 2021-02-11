import math
import random as r
import matplotlib.pyplot as plt
import csv 

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
        if xAvg[i] == 0:
            continue
        else:
            yLog.append(xAvg[i]*math.log(xAvg[i],2))

    plt.subplot(2, 2, 1)
    plt.plot(xAvg,yAvg)
    plt.xlabel('Size of Input')
    plt.ylabel('Number of comparisions')
    plt.grid(True)
    plt.title('Average Case')
    plt.legend(['Average Case'])

    plt.subplot(2, 2, 2)
    plt.plot(xBest,yBest, 'r')
    plt.xlabel('Size of Input')
    plt.ylabel('Number of comparisions')
    plt.grid(True)
    plt.title('Best Case')
    plt.legend(['Best Case'])

    plt.subplot(2, 2, 3)
    plt.plot(xWorst,yWorst, 'y')
    plt.xlabel('Size of Input')
    plt.ylabel('Number of comparisions')
    plt.grid(True)
    plt.title('Worst Case')
    plt.legend(['Worst Case'])

    plt.subplot(2, 2, 4)
    plt.plot(xAvg, yLog, 'g')
    plt.xlabel('Size of Input')
    plt.ylabel('Number of comparisions')
    plt.grid(True)
    plt.title('nlogn')
    plt.legend(['nlogn'])

    #plt.legend(['Average Case', 'Best Case', 'Worst Case', 'nlogn'])

    plt.subplots_adjust(hspace=0.4)
    plt.suptitle('HeapSort Cases', fontsize = 20)
    plt.show()

def parent(i):
	return math.floor(i/2)

def left(i):
	return 2*i+1

def right(i):
	return 2*i+2

def maxHeapify(arr, n, i):

	noOfComps = 0;
	x = 0

	l = left(i)
	r = right(i)
	
	largest = i

	noOfComps += 1
	if l < n and arr[l] > arr[i]:
		largest = l
		noOfComps += 1

	noOfComps += 1
	if r < n and arr[r] > arr[largest]: 
		largest = r
		noOfComps += 1

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		x = maxHeapify(arr, n, largest)

	#print('X = {0}, Comps = {1}, \n\tx + noOfComps = {2}'.format(x, noOfComps, (x + noOfComps)))
	
	return (x + noOfComps)

def heapSort(arr):
	
	comps1 = 0
	comps2 = 0
	
	n = len(arr)
	
	for i in range(n//2-1, -1, -1):
		comps1 += maxHeapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		comps2 += maxHeapify(arr, i, 0)

	print('Comps1 = {0}, Comps2 = {1}'.format(comps1, comps2))
	return (comps1 + comps2)

def best_case():

	inpComp = []
	runs = 100

	while(runs > 0):
		x = 0
		noOfInp = r.randint(0, 1000) #input size
		a = [int(i*r.random()) for i in range(2, noOfInp)]
		a.sort()
		x = heapSort(a) #comparisions

		inpComp.append((noOfInp, x))
		runs -= 1

	return inpComp

def avg_case():

	inpComp = []
	runs = 100

	while(runs > 0):
		x = 0
		noOfInp = r.randint(0, 1000) 
		a = [int(i*r.random()) for i in range(2, noOfInp)]
		x = heapSort(a)

		inpComp.append((noOfInp, x))
		runs -= 1

	return inpComp

def worst_case():

	inpComp = []
	runs = 100

	while(runs > 0):
		x = 0
		noOfInp = r.randint(0, 1000) #input size
		a = [int(i*r.random()) for i in range(2, noOfInp)]
		a.sort(reverse = True)
		x = heapSort(a) #comparisions

		inpComp.append((noOfInp, x))
		runs -= 1

	return inpComp


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
