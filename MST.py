from collections import Counter
from heapq import heappush, heappop
from Queue import Queue

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def __repr__(self):
        return 'Edge instance: ' + str(self.v) + ', ' + str(self.w) + ', ' + str(self.weight)
    
    def either(self):
        return self.v
    
    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            return None
    
    def __lt__(self, that):
        return self.weight < that.getWeight()
    
    def getWeight(self):
        return self.weight

class EdgeWeightedGraph:
    
    def __init__(self, filename):
        with open(filename) as f:
            self.V = int(f.readline())
            self.E = int(f.readline())
            self.adj = [0] * self.V
            for v in range(self.V):
                self.adj[v] = Counter()
            for line in f:
                line = line.split()
                v, w, weight = int(line[0]), int(line[1]),float(line[2])
                self.addEdge(Edge(v, w, weight))
    
    def getV(self):
        return self.V

    def getE(self):
        return self.E   
    
    def addEdge(self, e):
        v = e.either() 
        w = e.other(v)
        self.adj[v][e] += 1
        self.adj[w][e] += 1
        return
    
    def getAdj(self, v):
        return self.adj[v]
    
    def getEdges(self):
        bag = Counter()
        for v in range(self.V):
            for edge in self.adj[v]:
                if edge.other(v) > v:
                    bag[edge] += 1
        return bag

class UF:
    def __init__(self, N):
        self.parent = range(N)
        self.size = [1] * N
        self.numberOfTrees = N
    def root(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        if self.connected(p, q):
            return
         
        self.numberOfTrees -= 1
         
        if self.size[rootp] < self.size[rootq]:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]

class KruskalMST:
    def __init__(self, G):
        self.pq = []
        self.mst = []
        self.uf = UF(G.getV())
        for edge in G.getEdges():
            heappush(self.pq, edge)
        while len(self.pq) is not 0 and len(self.mst) < G.getV() - 1:
            e = heappop(self.pq)
            v = e.either()
            w = e.other(v)
            if self.uf.connected(v, w):
                continue
            self.uf.union(v, w)
            self.mst.append(e)
    def getEdges(self):
        return self.mst

# In the book, Queue was used to hold the MST.
class KruskalMST_Q:
    def __init__(self, G):
        self.pq = []
        self.mst = Queue()
        self.uf = UF(G.getV())
        for edge in G.getEdges():
            heappush(self.pq, edge)
        while len(self.pq) is not 0 and self.mst.qsize() < G.getV() - 1:
            e = heappop(self.pq)
            v = e.either()
            w = e.other(v)
            if self.uf.connected(v, w):
                continue
            self.uf.union(v, w)
            self.mst.put(e)
    def getEdges(self):
        return self.mst

import time
class LazyPrimMST:
    def __init__(self, G):
        self.marked = set() # or just use self.marked = [False] * G.getV()
        self.mst = []
        self.pq = []

        self.visit(G, 0)

        while len(self.pq) is not 0: # or while self.pq:
            print self.pq
            time.sleep(1)
            e = heappop(self.pq)
            v = e.either()
            w = e.other(v)
            if v in self.marked and w in self.marked: # don't forgeet to add self. otherwise self.pq will get infinitely long
                continue
            self.mst.append(e)
            if v not in self.marked:
                self.visit(G, v)
            if w not in self.marked:
                self.visit(G, w)

    def visit(self, G, v):
        self.marked.add(v)
        for edge in G.getAdj(v):
            if edge.other(v) not in self.marked:
                heappush(self.pq, edge)

    def getEdges(self):
        return self.mst

