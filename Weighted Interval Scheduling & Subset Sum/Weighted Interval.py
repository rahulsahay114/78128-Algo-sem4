class node:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit
 
 
# Function to find the maximum profit of non-overlapping nodes using LIS
def findMaxProfit(nodes):
 
    # sort the nodes according to increasing order of their start time
    nodes.sort(key=lambda x: x.start)
 
    # `maxProfit[i]` stores the maximum profit of non-conflicting nodes
    # ending at the i'th node
    maxProfit = [None] * len(nodes)
 
    # consider every node
    for i in range(len(nodes)):
        # initialize current profit to 0
        maxProfit[i] = 0
 
        # consider each `j` less than `i`
        for j in range(i):
            # if the j'th node is not conflicting with the i'th node and
            # is leading to the maximum profit
            if nodes[j].finish <= nodes[i].start and maxProfit[i] < maxProfit[j]:
                maxProfit[i] = maxProfit[j]
 
        # end the current task with i'th node
        maxProfit[i] += nodes[i].profit
 
    # return the maximum profit
    return max(maxProfit)
 
 
if __name__ == '__main__':
 
    nodes = [
        node(0, 6, 60), node(5, 9, 50), node(1, 4, 30),
        node(5, 7, 30), node(3, 5, 10), node(7, 8, 10)
    ]
 
    print("The maximum profit is", findMaxProfit(nodes))