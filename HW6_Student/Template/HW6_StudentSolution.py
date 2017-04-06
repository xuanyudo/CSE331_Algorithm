def HW6_StudentSolution(rallies):
    for index in range(len(rallies)):
        rallies[index]=(index, )+rallies[index]
    sortedlist = sorted(rallies,key = lambda rally:rally[2])
    totalTime = 0
    answer=[]
    for item in sortedlist:
        answer.append((item[0],totalTime))
        totalTime+=item[1]
        if totalTime>item[2]:
            return []
    return answer #return empty list for now
	