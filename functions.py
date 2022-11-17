import numpy as np
from Branch import Branch
from typing import List
from DSU import DSU

np.set_printoptions(suppress=True)

def find_cl(AT, AL):
    AT_Inverse = np.linalg.inv(AT)
    CL = np.dot(AT_Inverse , AL)
    return CL

def find_b(CL):
    BT = -1 * np.matrix.transpose(CL)
    BT_Matrix = np.matrix(BT)
    rows,columns = BT_Matrix.shape
    Identity_Matrix = np.eye(rows)
    Buff = []
    for i in range(rows):
        Buff.append(list(np.concatenate((BT[i] , Identity_Matrix[i]))))
    B = np.matrix(Buff)
    return B


if __name__ == '__main__':
    AT = [[-1, 1, 1],
          [0, 0, -1],
          [1, 0, 0]]
    AL = [[1, 0],
          [0, 0],
          [-1, -1]]
    CL = find_cl(AT, AL)
    print(CL)
    print(find_b(CL))

def buildTree(N: int, branches: List(Branch)):
    #Generates AT and AL
    AT= [[] for i in range(N)]
    AL= [[] for i in range(N)]
    dsu= DSU(N)
    for branch in branches:
        start, end= branch.start, branch.end
        if dsu.sameGroup(u, v):
            for i in range(N - 1):
                AL[i].append(0)
            
            AL[start]= 1
            AL[end]= -1
        
        else:
            dsu.union(start, end)
            for i in range(N - 1):
                AT[i].append(0)

            AT[start]= 1
            AL[end]= -1
    
    AT.pop()
    AL.pop()
    return {AT: AT, AL: AL}