import random as r
import math
import matplotlib.pyplot as plt
tot = [] #list of number of comparisons made in different runs of insertion sort.
inps = []

ListOfInpSizeAndComps = []

def inssort(a):

	noOfComp = 0
	for i in range(len(a)):
		
		j = i - 1
		temp = a[i]

		while(j >= 0 and a[j] > temp):
			
			noOfComp += 1
			a[j+1] = a[j]
			j -= 1

		a[j+1] = temp

	return noOfComp #returns number of comparisions made

def plot(lst):
	
	x = [] 
	y = [] 
	yLog = []

	lst.sort() #sorting by size of inputs.
	
	for i in range(len(lst)):
		x.append(lst[i][0]) #'size of inputs' extracted.
		y.append(lst[i][1])

	
	for i in range(len(x)):
		yLog.append(x[i]*math.log(x[i],2))



	plt.plot(x,y)
	plt.plot(x, yLog, 'g--')
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
		x = inssort(a) #comparisions

		ListOfInpSizeAndComps.append((noOfInp, x))
		
		noOfRuns -= 1

	#print('List of Comparisons made in each run: \n{}'.format(tot))
	#print('\nTotal Runs: {}'.format(len(tot)))

	plot(ListOfInpSizeAndComps)

main()

