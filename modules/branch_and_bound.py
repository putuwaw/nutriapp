import graphviz
import time

# global variables
N = 0
W = 0
w = []
p = []
pPerW = []

# class priority queue
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0
    # enqueue with priority (bound)
    def enqueue(self, node):
        if (self.size == 0):
            self.queue.append(node)
        else:
            saveI = 0
            for i in range(self.size):
                if node.bound > self.queue[i].bound:
                    saveI = i
                    break
            self.queue.insert(saveI, node)
        self.size += 1
    # dequeue like normal queue (front)
    def dequeue(self):
        result = self.queue.pop(0)
        self.size -= 1
        return result

# class node
class Node:
    def __init__(self, level, profit, weight, bound=0, number=0, items=[]):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
        self.number = number
        self.items = items

# function to get bound for node
def get_bound(node):
    global N, W, w, p, pPerW
    # if weight is already over limit or leaf node
    if node.weight >= W or node.level >= N-1:
        return 0
    else:
        result = node.profit
        j = node.level + 1
        weightLeft = W - node.weight
        result += pPerW[j] * weightLeft
        return result

# main function
def solve(limit, detail):
    # start time
    startTime = time.time()
    # access global variables
    global N, W, w, p, pPerW, Node, PriorityQueue
    N = 0
    W = 0
    w.clear()
    p.clear()
    pPerW.clear()
    # remove newline
    detailList = detail.replace("\r\n", ", ").split(", ")
    # convert to float
    for i in range(len(detailList)):
        if i % 3 != 0:
            detailList[i] = float(detailList[i])
    # initialize variables
    N = len(detailList) // 3
    W = float(limit)
    detailList = [detailList[i:i+3] for i in range(0, len(detailList), 3)]
    dupDetailList = detailList.copy()
    tempDict = {}
    for i in range(N):
        tempDict[i] = detailList[i][2] / detailList[i][1]
    sortedDict = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    detailList.clear()
    for i in range(N):
        detailList.append(dupDetailList[sortedDict[i][0]])
    for i in range(N):
        w.append(detailList[i][1])
        p.append(detailList[i][2])
        pPerW.append(sortedDict[i][1])
    # initialize priority queue
    pq = PriorityQueue()
    # initialize root node
    v = Node(-1, 0, 0)
    v.bound = get_bound(v)
    # enqueue root node
    pq.enqueue(v)
    # initialize utils variable
    maxProfit = 0
    selectedItems = []
    nodeNumber = 0
    # graph
    g = graphviz.Digraph(name="Branch and Bound")
    # best-first search
    while(pq.size > 0):
        v = pq.dequeue()
        if (v.bound > maxProfit):
            # make child node (with)
            u = Node(v.level + 1, v.profit + p[v.level+1], v.weight+w[v.level+1])
            nodeNumber += 1
            u.bound = get_bound(u)
            u.number = nodeNumber
            u.items = v.items.copy()
            u.items.append(u.level)
            # calculate max profit
            if u.weight <= W and u.profit > maxProfit:
                maxProfit = u.profit
                selectedItems = u.items.copy()
            # make child node (without)
            uo = Node(u.level, v.profit, v.weight)
            nodeNumber += 1
            uo.bound = get_bound(uo)
            uo.number = nodeNumber
            uo.items = v.items.copy()
            # enqueue child nodes
            if uo.bound > maxProfit:
                pq.enqueue(uo)
            if u.bound > maxProfit:
                pq.enqueue(u)
            # drawing graph
            strU = "ub="+str(u.bound)+ ", v="+str(u.profit)+", w="+ str(u.weight) + " (" + str(u.number) + ")"
            strUO = "ub="+str(uo.bound)+ ", v="+str(uo.profit)+", w="+ str(uo.weight) + " (" + str(uo.number) + ")"
            strV = "ub="+str(v.bound)+ ", v="+str(v.profit)+", w="+ str(v.weight) + " (" + str(v.number) + ")"
            if (u.level == 0):
                g.edge(strV, strU, label="dengan "+detailList[u.level][0])
                g.edge(strV, strUO, label="tanpa "+detailList[u.level][0])
            else:
                g.edge(strV, strU, label="dengan "+detailList[u.level][0])
                g.edge(strV, strUO, label="tanpa "+detailList[u.level][0])
    # result
    resultList = []
    # 0 -> max profit
    resultList.append(maxProfit)
    # 1 -> selected items
    tempList = []
    for i in selectedItems:
        tempList.append(detailList[i][0])    
    resultList.append(tempList)
    # 2 -> graph
    resultList.append(g)
    # 3 -> time
    totalTime = time.time() - startTime
    resultList.append(totalTime)
    # return value
    return resultList