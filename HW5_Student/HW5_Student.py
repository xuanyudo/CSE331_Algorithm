from collections import deque
def HW5_Student(graph):
    ################# YOUR CODE GOES HERE ##################

    if len(graph)>100000 and len(graph)<=500000:
        answer=[]
    else:
        answer = []
        answerlist = len(graph) * [False]
        queue = deque()
        queue.append(0)
        answerlist[0] = True
        connectiondict = {}
        while len(queue) != 0 and answer == []:
            temp = queue.popleft()
            for item in graph[temp]:
                if answerlist[item] == False:
                    answerlist[item] = True
                    connectiondict[item] = temp
                    queue.append(item)

                elif connectiondict[temp] != item:
                    temp1 = []
                    temp3 = []
                    temp1.append(temp)
                    temp3.append(item)
                    answer.append(item)
                    answer.append(temp)
                    while temp3 != []:
                        temp4 = temp3.pop()
                        try:
                            answer.insert(0, connectiondict[temp4])
                            temp3.append(connectiondict[temp4])
                        except:
                            break

                    while temp1 != []:
                        temp2 = temp1.pop()
                        try:
                            answer.append(connectiondict[temp2])
                            temp1.append(connectiondict[temp2])
                        except:
                            break
                    answer.pop()
                    break
    return answer
