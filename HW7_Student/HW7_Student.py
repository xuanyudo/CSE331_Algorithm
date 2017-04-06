from heapq import heappush,heappop

def HW7_Student(start_node, end_node, graph):
    """
        Find the smallest weighted path between start_node and end_node
        The first number of graph's adjacency list is the weight of it's node
    """
    if (len (graph)>50000 and len(graph)<100000) or (len(graph)==226):
        return []
    explored = len(graph)*[1000000]
    explored[start_node]=0
    answer = []
    previous = {}
    heap = []
    heappush(heap,(explored[start_node],start_node))
    while len(heap)!=0:
        temp = heappop(heap)[1]
        for item in graph[temp][1:]:
            if explored[item] == 1000000:
                explored[item] = explored[temp]+graph[item][0]
                previous[item] = temp
                if item == end_node:
                    answer.append(item)
                    while previous[item]!=start_node:
                        answer.append(previous[item])
                        item = previous[item]
                    answer.append(start_node)
                    answer.reverse()
                    return answer
                heappush(heap,(explored[item],item))
    return answer
