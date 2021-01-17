import random as r
import math
import matplotlib.pyplot as plt
tot = [] 
inps = []

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
	plt.plot(xBest,yBest, 'r.-')
	plt.plot(xWorst,yWorst, 'y')
	plt.plot(xAvg, yLog, 'g--')
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
		noOfInp = r.randint(100, 600) #input size
		a = [int(i*r.random()) for i in range(noOfInp)]
		x = inssort(a) #comparisions

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
		noOfInp = r.randint(100, 600) #input size
		a = [int(i*r.random()) for i in range(noOfInp)]
		a.sort(reverse = True)
		x = inssort(a) #comparisions

		ListOfInpSizeAndComps.append((noOfInp, x)) #list of tuples.
		
		noOfRuns -= 1

	return ListOfInpSizeAndComps

def best_case():

	ListOfInpSizeAndComps = [] #list of number of comparisons made in different runs of insertion sort.

	noOfRuns = r.randint(10, 100) #deciding the total number of runs to be made

	while(noOfRuns > 0):
		
		x = 0
		noOfInp = r.randint(100, 600) #input size
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

main()

