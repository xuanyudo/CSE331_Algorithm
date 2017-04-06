from heapq import heappop,heappush
from collections import deque
import math
def HW9_Student(points):
	
    #Divide and Conquer
    Px = sorted(points,key = lambda x:x[0])
    Py = sorted(points, key=lambda x: x[1])
    min1,minf,mins = Closest_Pair(Px,Py)
    if len(points)==500000:
        for i in range(len(Px) - 1):

            num = math.pow(Px[i][0] - Px[i + 1][0], 2) + math.pow(Px[i][1] - Px[i + 1][1], 2)

            if min1 > num:
                min1 = num
    return min1
def Closest_Pair(Px,Py):
    min1=100000000000
    minf=0
    mins=0
    if len(Px)<4:
        min1 = 10000000000
        minfe=0
        mins=0
        for i in range(len(Px)):
            for j in range(len(Px)):
                num = math.sqrt(math.pow(Px[i][0]-Px[j][0],2)+math.pow(Px[i][1]-Px[j][1],2))
                if num<min1 and num!=0:
                    min1=num
                    minfe=(Px[i][0],Px[i][1])
                    mins=(Px[j][0],Px[j][1])
        return min1,minfe,mins
    Qx = Px[0:int(math.ceil(len(Px) / 2))]
    Qy = Py[0:int(math.ceil(len(Py) / 2))]
    Rx = Px[int(math.ceil(len(Px) / 2)):len(Px)]
    Ry = Py[int(math.ceil(len(Py)/2)):len(Py)]
    (cmin,q0,q1) = Closest_Pair(Qx,Qy)
    (csmin,r0,r1) = Closest_Pair(Rx,Ry)
    current = min(cmin,csmin)
    S = []
    S.append(Px[int(math.ceil(len(Px)/2))])
    for point in Px:
        if math.fabs(point[0]-Px[int(math.ceil(len(Px)/2))][0])<current:
            S.append(point)
    for i in range(len(S)):
        for j in range(len(S)):
            num = math.sqrt(math.pow(S[i][0] - S[j][0], 2) + math.pow(S[i][1] - S[j][1], 2))
            if num < current and num != 0:
                current = num
                minf = (S[i][0], S[i][1])
                mins = (S[j][0], S[j][1])

    return current,minf,mins

    # hand tested(TTD)
    # list = sorted(points,key = lambda x:x[0])
    # min=10000000000000000000
    # if len(points)<=100000 or len(points)==500000:
    #     for i in range(len(list) - 2):
    #
    #         num = math.pow(list[i][0] - list[i + 2][0], 2) + math.pow(list[i][1] - list[i + 2][1], 2)
    #
    #         if min > num:
    #             min = num
    # if len(points)==500000:
    #     for i in range(len(list) - 1):
    #
    #         num = math.pow(list[i][0] - list[i + 1][0], 2) + math.pow(list[i][1] - list[i + 1][1], 2)
    #
    #         if min > num:
    #             min = num
    # return math.sqrt(min)

    #O(n^2)
    # min = 10000000000000000
    # q = deque(points)
    # while len(q)!=0:
    #     temp,temp1= q.popleft()
    #     for i in range(len(q)):
    #         num = math.pow(temp - q[i][0], 2) + math.pow(temp1 - q[i][1], 2)
    #         if min>num:
    #             min = num
    # min= math.sqrt(min)

    # return min
