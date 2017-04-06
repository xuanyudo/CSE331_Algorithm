from collections import deque
def HW4_Student(start_node, graph):
    # BFS Algorithm
    queue=deque()
    answerlist=len(graph)*[-1]
    answerlist[start_node]=0
    queue.append(start_node)
    while len(queue)!=0:
        temp=queue.popleft()
        for item in graph[temp]:
            if answerlist[item]==-1:
                answerlist[item]=answerlist[temp]+1
                queue.append(item)
    return answerlist #Return empty


    # BFS Algorithm using array
    # alist=[]
    # answerlist = []
    # for node in graph:
    #     if node in graph[start_node]:
    #         answerlist.append(1)
    #         alist.append(node)
    #     else:
    #         answerlist.append(-1)
    # answerlist[start_node] = 0
    # while len(alist) != 0:
    #     temp = alist.pop(0)
    #     for item in graph[temp]:
    #         if answerlist[item] == -1:
    #             answerlist[item] = answerlist[temp]+1
    #             alist.append(item)
    # return answerlist  # Return empty
#
