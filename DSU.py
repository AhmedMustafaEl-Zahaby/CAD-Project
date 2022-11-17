class DSU:
    def __init__(self, n):
        self.parents= [i for i in range(n)]
    
    def findSet(self, x):
        if self.parents[x] != x:
            self.parents[x]= self.findSet(self.parents[x])
        
        return self.parents[x]


    def sameGroup(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def union(self, x, y):
        x, y= self.findSet(x), self.findSet(y)
        self.parents[x]= y
    
