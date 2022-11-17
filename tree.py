import numpy as np

tree_nodes = []
tree_linkes = []
graph = []
N = 4
visited = [0 for i in range(300)]


def find_Tree(idx):
    global tree_nodes, tree_linkes, graph, visited, N

    if visited[idx] == 1:
        return

    visited[idx] = 1

    tree_nodes.append(idx)

    for i in graph[idx]:
        if visited[i] == 0 and i not in tree_nodes:
            find_Tree(i)

    visited[idx] = 0
    tree_nodes.remove(idx)


def solve():
    global graph, tree_nodes, branches
    numberOfBranshes = int(input())
    graph = [[] for i in range(10)]
    branches = []
    for i in range(numberOfBranshes):
        first_node, second_node = list(map(int, input().split()))
        graph[first_node].append(second_node)
        tree_linkes.append([first_node, second_node])
        branches.append([first_node, second_node])

    find_Tree(1)

    for i in range(1, len(tree_nodes)):
        tree_linkes.remove([tree_nodes[i - 1], tree_nodes[i]])

    A = np.zeros((numberOfBranshes,6))
    for i in range(len(branches)):
        A[branches[i][0]][i] = 1
        A[branches[i][1]][i] = -1


    Buff_Matrix = np.array(A)
    # Indeceny_Matrix = np.delete(Buff_Matrix , [0, 5], axis=0)
    print(Buff_Matrix)


if __name__ == '__main__':
    solve()

