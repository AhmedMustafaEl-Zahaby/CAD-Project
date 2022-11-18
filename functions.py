import numpy as np
from Branch import Branch
from typing import List
from DSU import DSU


def buildTree(N, branches):
    #Generates AT and AL
    AT= [[] for i in range(N)]
    AL= [[] for i in range(N)]

    dsu= DSU(N)
    for branch in branches:
        start, end= branch.start, branch.end
        if dsu.sameGroup(start, end):
            for i in range(N):
                d= 0
                if i == start:
                    d= 1
                elif i == end:
                    d= -1
                AL[i].append(d)
        
        else:
            dsu.union(start, end)
            for i in range(N):
                d= 0
                if i == start:
                    d= 1
                elif i == end:
                    d= -1
                AT[i].append(d)

    AT.pop()
    AL.pop()
    return [AT, AL]

def find_IB(branches):
    Buff = []
    for i in branches:
        Buff.append(i.I)
    IB = np.rot90(np.rot90(np.rot90(np.matrix(Buff))))
    return IB


def find_EB(branches):
    Buff = []
    for i in branches:
        Buff.append(i.V)
    EB = np.rot90(np.rot90(np.rot90(np.matrix(Buff))))
    return EB


def find_ZB(branches):
    ZB = np.zeros((len(branches) , len(branches)))
    for i in range(len(branches)):
        ZB[i][i] = branches[i].R
    return ZB


def find_CL(AT, AL):
    AT_Inverse = np.linalg.inv(AT)
    CL = np.dot(AT_Inverse , AL)
    return CL


def find_BT(CL):
    BT = -1 * np.matrix.transpose(CL)
    return BT


def find_B(BT):
    BT_Matrix = np.matrix(BT)
    rows,columns = BT_Matrix.shape
    Identity_Matrix = np.eye(rows)
    Buff = []
    for i in range(rows):
        Buff.append(list(np.concatenate((BT[i] , Identity_Matrix[i]))))
    B = np.matrix(Buff)
    return B

def find_BTranspose(B):
    B_Transpose = np.matrix.transpose(B)
    return B_Transpose

def find_IL(N , branches):
    AT,AL = buildTree(N, branches)
    CL = find_CL(AT , AL)
    BTree = find_BT(CL)
    B = find_B(BTree)
    BT = find_BTranspose(B)
    ZB = find_ZB(branches)
    IB = find_IB(branches)
    EB = find_EB(branches)
    #first term = B * ZB
    first_term = np.dot(B , ZB)
    #second term = B * ZB * IB
    second_term = np.dot(first_term , IB)
    #third term = B * EB
    third_term = np.dot(B , EB)
    # return first_term
    divisor = np.linalg.inv(np.dot(first_term , BT))
    IL = np.matmul(divisor,third_term)
    return [IL,BT]

def find_JB(N , brances):
    IL,BT = find_IL(N , brances)
    JB = np.dot(BT , IL)
    return JB

def find_VB(N , branches):
    JB = find_JB(N , branches)
    ZB = find_ZB(branches)
    VB = np.dot(ZB , JB)
    return VB

if __name__ == '__main__':
    pass

