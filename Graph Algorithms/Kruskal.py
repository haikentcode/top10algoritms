import unittest
from UnionFind import UnionFind
from Graphs import isUndirected

def MinimumSpanningTree(G):
    if not isUndirected(G):
        raise ValueError("MinimumSpanningTree: input is not undirected")
    for u in G:
        for v in G[u]:
            if G[u][v] != G[v][u]:
                raise ValueError("MinimumSpanningTree: asymmetric weights")
    subtrees = UnionFind()
    tree = []
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree

class MSTTest(unittest.TestCase):
    def testMST(self):
        G = {0:{1:11,2:13,3:12},1:{0:11,3:14},2:{0:13,3:10},3:{0:12,1:14,2:10}}
        T = [(2,3),(0,1),(0,3)]
        for e,f in zip(MinimumSpanningTree(G),T):
            self.assertEqual(min(e),min(f))
            self.assertEqual(max(e),max(f))

if __name__ == "__main__":
    unittest.main()
