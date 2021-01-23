import random as r
import math
import matplotlib.pyplot as plt
import csv
import numpy as np

def inssort(a):

	noOfComp = 0

	for i in range(1, len(a)):
		
		j = i - 1
		temp = a[i]

		while(j >= 0 and a[j] > temp):
			
			noOfComp += 1
			a[j+1] = a[j]
			j -= 1

		a[j+1] = temp

	return noOfComp #returns number of comparisions made

def plot(lstBest, lstAvg, lstWorst):
    
    xAvg = [] 
    yAvg = [] 

    xBest = [] 
    yBest = [] 

    xWorst = [] 
    yWorst = [] 

    xLog = []
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

    xLog = np.array(xAvg[::])
    yLog = np.array(yLog[::])

    plt.subplot(2, 2, 1)
    plt.plot(xAvg,yAvg)
    plt.xlabel('Size of Input')
    plt.ylabel('Number of Comparisions')
    plt.grid(True)
    plt.title('Average Case')
    plt.legend(['Average Case'])

    plt.subplot(2, 2, 2)
    plt.plot(xBest,yBest, 'r')
    plt.xlabel('Size of Input')
    plt.ylabel('Number of Comparisions')
    plt.grid(True)
    plt.title('Best Case')
    plt.legend(['Best Case'])

    plt.subplot(2, 2, 3)
    plt.plot(xWorst,yWorst, 'y')
    plt.xlabel('Size of Input')
    plt.ylabel('Number of Comparisions')
    plt.grid(True)
    plt.title('Worst Case')
    plt.legend(['Worst Case'])

    plt.subplot(2, 2, 4)
    plt.plot(xLog, yLog, 'g')
    plt.xlabel('Size of Input')
    plt.ylabel('Number of Comparisions')
    plt.grid(True)
    plt.title('nlogn')
    plt.legend(['nlogn'])

    #plt.legend(['Average Case', 'Best Case', 'Worst Case', 'nlogn'])

    plt.subplots_adjust(hspace=0.4)
    plt.suptitle('Insertion Sort Cases', fontsize = 20)
    plt.show()

def avg_case():
	
	ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

	noOfRuns = 500 #r.randint(10, 100) #deciding the total number of runs to be made

	while(noOfRuns > 0):
		
		x = 0
		noOfInp = r.randint(0, 600) #input size
		a = [int(i*r.random()) for i in range(noOfInp)]
		x = inssort(a) #comparisions

		ListOfInpSizeAndComps.append((noOfInp, x)) #list of tuples.
		
		noOfRuns -= 1

	#print('List of Comparisons made in each run: \n{}'.format(tot))
	#print('\nTotal Runs: {}'.format(len(tot)))

	return ListOfInpSizeAndComps

def worst_case():
	
	ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

	noOfRuns = 500 #r.randint(10, 100) #deciding the total number of runs to be made

	while(noOfRuns > 0):
		
		x = 0
		noOfInp = r.randint(0, 600) #input size
		a = [int(i*r.random()) for i in range(noOfInp)]
		a.sort(reverse = True)
		x = inssort(a) #comparisions

		ListOfInpSizeAndComps.append((noOfInp, x)) #list of tuples.
		
		noOfRuns -= 1

	return ListOfInpSizeAndComps

def best_case():

	ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

	noOfRuns = 500 #r.randint(10, 100) #deciding the total number of runs to be made

	while(noOfRuns > 0):
		
		x = 0
		noOfInp = r.randint(0, 600) #input size
		a = [int(i*r.random()) for i in range(noOfInp)]
		a.sort()
		x = inssort(a) #comparisions

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

	with open('data_insertionSort.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(allLists)

main()

