import random as r

def countingSort(arr, digit):
	n = len(arr)
	output = [0]*n
	count = [0]*10

	for i in range(0, n):
		
		index = arr[i]/digit
		count[int(index%10)] += 1

	for i in range(1,10):
		count[i] += count[i-1]

	i = n-1
	while i>=0:
		index = arr[i]/digit
		output[count[int(index % 10)] - 1] = arr[i]
		count[int(index % 10)] -= 1
		i -= 1

	i=0
	for i in range(0, len(arr)):
		arr[i] = output[i]

def radixSort(arr):

	m = max(arr)

	digit = 1
	while m/digit > 0:
		countingSort(arr, digit)
		digit = digit*10

def main():

	arr = [x * r.randint(1,20) for x in range(1,10)]
	radixSort(arr)

	print(arr)