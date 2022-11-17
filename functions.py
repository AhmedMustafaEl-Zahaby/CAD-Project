import numpy as np
from Branch import Branch
from typing import List
from DSU import DSU

def find_CL(AT, AL):
    AT_Inverse = np.linalg.inv(AT)
    CL = np.dot(AT_Inverse , AL)
    return CL


def find_BT(CL):
    BT = -1 * np.matrix.transpose(CL)


def find_B(BT):
    BT_Matrix = np.matrix(BT)
    rows,columns = BT_Matrix.shape
    Identity_Matrix = np.eye(rows)
    Buff = []
    for i in range(rows):
        Buff.append(list(np.concatenate((BT[i] , Identity_Matrix[i]))))
    B = np.matrix(Buff)
    return B

def find_IL(B , ZB , IB , EB , BT):
    #first term = B * ZB
    first_term = np.dot(B , ZB)
    #second term = B * ZB * IB
    second_term = np.dot(first_term , IB)
    #third term = B * EB
    EB_matrix = np.rot90(np.rot90(np.rot90(np.matrix(EB))))
    third_term = np.dot(B , EB_matrix)
    divisor = np.linalg.inv(np.dot(first_term , BT))
    IL = np.matmul(divisor,third_term)
    return IL

def find_JB(BT , IL):
    JB = np.dot(BT , IL)
    return  JB

def find_VB(ZB , JB):
    VB = np.dot(ZB , JB)
    return VB

if __name__ == '__main__':
    pass

