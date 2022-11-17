from Branch import Branch
from functions import *

def test1():
    N= 4
    branches= []

    branches.append(Branch(2, 0, 0, 0, 0))
    branches.append(Branch(0, 1, 0, 0, 0))
    branches.append(Branch(1, 2, 0, 0, 0))
    branches.append(Branch(1, 3, 0, 0, 0))
    branches.append(Branch(2, 3, 0, 0, 0))
    branches.append(Branch(3, 0, 0, 0, 0))

    AT, AL= buildTree(N, branches)
    print(AT, AL)

def test2():
    B = [[1 , 1 , 0 , 1 , 0 , 0],
         [0 , -1 , 1 , 0 , 1 , 0],
         [1 , 1 , -1 , 0 , 0 , 1]]
    BT = [[1 , 0 , 1],
          [1 , -1 ,1],
          [0 , 1 , -1],
          [1 , 0 , 0],
          [0 , 1 , 0],
          [0 , 0 , 1]]
    ZB = [[5 , 0 , 0 , 0 , 0 , 0],
          [0 , 10 , 0 , 0 , 0 , 0],
          [0 , 0 , 5 , 0 , 0 , 0],
          [0 , 0 , 0 , 5 , 0 , 0],
          [0 , 0 , 0 , 0 , 5 , 0],
          [0 , 0 , 0 , 0 , 0 , 10]]
    EB = [50,0,0 , 0 , 0 , 0]
    print(find_VB(ZB , find_JB(BT , find_IL(B , ZB , 0 , EB , BT))))


test1()
