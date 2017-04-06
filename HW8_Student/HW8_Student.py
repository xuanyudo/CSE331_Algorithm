from heapq import heappush,heappop

def HW8_Student(graph):
    """
        Find the MST of the graph. Graph is given in adjacency matrix 'graph'
    """
    answer = []
    parent = [-1]*len(graph)
    explored = [False]*len(graph)
    heap= []
    cost = [1000000]*len(graph)
    heappush(heap,(parent[0],0))
    explored[0] = True
    cost[0]=0
    while len(heap)!=0:
        tempp,temp = heappop(heap)

        explored[temp] = True
        for index in range(len(graph[temp])):
            if cost[index] > graph[temp][index] and graph[temp][index] != -1 and explored[index] == False:
                cost[index] = graph[temp][index]
                heappush(heap, (cost[index], index))
                parent[index] = temp

    return parent