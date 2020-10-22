class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        # The rank can be by size of the trees as rank or depth of the tree
        self.rank = [1] * n
        self.parent = list(range(n))

    # Find(A) == Find(B) - check if two objects A and B are in same component or not.
    def find(self, x):
        # Find the representative of the set (root vertex)
        if self.parent[x] != x:
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset != yset:
            # Put smaller ranked item under
            # bigger ranked item if ranks are
            # different
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset

            elif self.rank[xset] > self.rank[yset]:
                self.parent[yset] = xset

            # If ranks are same, then move y under
            # x (doesn't matter which one goes where)
            # and increment rank of x's tree
            else:
                self.parent[yset] = xset
                self.rank[xset] = self.rank[xset] + 1


# https://cp-algorithms.com/data_structures/disjoint_set_union.html
obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
print(obj.find(4) == obj.find(0))  # True
print(obj.find(1) == obj.find(0))  # False
print(obj.find(4) == obj.find(3))  # False
print(obj.find(0) == obj.find(2))  # True
