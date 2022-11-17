from Branch import Branch
from functions import buildTree

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


