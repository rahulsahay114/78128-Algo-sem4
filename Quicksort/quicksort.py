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


    print(lstAvg)

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
    plt.suptitle('Quicksort Cases', fontsize = 20)
    plt.show()

class quick:

	noOfComps = 0

	def __init__(self):
		self.noOfComps = 0

	def partition(self, A, p, r):

		x = A[r] #pivot
		i = p-1
		
		quick.noOfComps += 1		
		for j in range(p, r):

			if A[j] <= x:
				i = i+1
				A[i], A[j] = A[j], A[i]

		A[i+1], A[r] = A[r], A[i+1]
		return (i+1)

	def quicksort(self, A, p, r):
		if len(A) == 1:
			return A

		if p < r: 
			q = self.partition(A, p ,r)
			self.quicksort(A, p, q-1)
			self.quicksort(A, q+1, r)

	def getComps(self):
		return quick.noOfComps
	 
	def setComps(self):
	 	quick.noOfComps = 0

def best_case():

	inpComp = []
	runs = 100
	q = quick()

	while(runs > 0):

		q.setComps()
		x = 0
		noOfInp = r.randint(0, 1000) #input size
		a = [int(i*r.random()) for i in range(2, noOfInp)]
		a.sort()
		q.quicksort(a, 0, len(a)-1)
		x = q.getComps() #comparisions

		inpComp.append((noOfInp, x))
		runs -= 1

	return inpComp

def worst_case():

	inpComp = []
	runs = 100
	q = quick()

	while(runs > 0):
		
		q.setComps()
		x = 0
		noOfInp = r.randint(0, 1000) #input size
		a = [int(i*r.random()) for i in range(2, noOfInp)]
		a.sort(reverse = True)
		q.quicksort(a, 0, len(a)-1) 
		x = q.getComps() #comparisons

		inpComp.append((noOfInp, x))
		runs -= 1

	return inpComp

def avg_case():

	inpComp = []
	runs = 100
	q = quick()

	while(runs > 0):

		q.setComps()
		x = 0
		noOfInp = r.randint(0, 1000) 
		a = [int(i*r.random()) for i in range(2, noOfInp)]
		q.quicksort(a, 0, len(a)-1)
		x = q.getComps() #comparisons

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

	with open('data_quicksort.csv', 'w') as file:
	        writer = csv.writer(file)
	        writer.writerows(allLists)

main()