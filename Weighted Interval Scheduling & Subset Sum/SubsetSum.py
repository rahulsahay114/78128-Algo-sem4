w = [2, 2, 3] #weights of items
n = len(w)
W = 6 #knapsack weight

M = [[0 for i in range(W+1)] for i in range(n+1)]

'''print('\nM: ')
for r in range(n+1):
	for c in range(W+1):
		print(M[r][c], end=' ')
	print()'''

#The leftmost column and bottom row is always 0.
for i in range(n+1):
 	M[i][0] = 0

for i in range(W+1):
	M[0][i] = 0

#starting from the row next 
#to the last row which was initialised to 0
#i.e we begin from 1 to n
for i in range(1, n+1):
	
	#starting from the column next 
	#to the last column which was initialised to 0
	#i.e we begin from 1 to W
	for j in range(1, W+1):
		
		#w[i-1] because index is offset by 1, w[1] is w[0]
		#as we start for-loop for 'i' from 1.
		#remove -1 from i-1 to understand the algo.
		if j < w[i-1]:
			M[i][j] = M[i-1][j]

		else:
			M[i][j] = max(M[i-1][j], w[i-1] + M[i-1][j- w[i-1]])



#Printing our solution array 
#starting from last row upto the first.
print('\nM: ')
for r in range(n, -1, -1):
		#print(M[r], end=' ')
		print(r, end='   ')
		for i in range(len(M[r])):
			print(M[r][i], end=' ')
		print()

print("\n  ", end='  ')
for i in range(W+1):
	print('{:>1}'.format(i), end=' ')
	#print(i, end='')
print()

print('\nOptimum solution: ', M[n][W])