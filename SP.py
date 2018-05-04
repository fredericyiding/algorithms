from collections import Counter
from heapq import heappush, heappop

class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def __repr__(self):
        return 'Directed Edge instance: ' + str(self.v) + '->' + str(self.w) + ', ' + str(self.weight)
    
    def start(self):
        return self.v
    
    def end(self):
        return self.w

    def __lt__(self, that):
        return self.weight < that.getWeight()
    
    def getWeight(self):
        return self.weight


class EdgeWeightedDiGraph:
    def __init__(self, filename):
        with open(filename) as f:
            self.V = int(f.readline())
            self.E = int(f.readline())
            self.adj = [0] * self.V
            for v in range(self.V):
                # the reason to use bag instead of set is to allow multiple routes
                self.adj[v] = Counter()  # each item of self.adj is a bag; and the self.getEdges() also returns a bag
            for line in f:
                line = line.split()
                v, w, weight = int(line[0]), int(line[1]),float(line[2])
                self.addEdge(DirectedEdge(v, w, weight))
    
    def getV(self):
        return self.V

    def getE(self):
        return self.E
    
    def addEdge(self, e):
        start = e.start() 
        self.adj[start][e] += 1
        return
    
    def getAdj(self, v):
        return self.adj[v]
    
    def getEdges(self):
        bag = Counter()  # can also be a list
        for v in range(self.V):
            for edge in self.adj[v]:
                    bag[edge] += 1
        return bag

class DijkstraSP:
    def __init__(self, G, s):
        self.s = s # s is the starting vertex, an integer
        self.edgeTo = [None] * G.getV()
        self.distTo = [float('inf')] * G.getV()
        self.distTo[s] = 0.0
        self.pq = []

        heappush(self.pq, (0.0, s))

        while self.pq:
            dist, v = heappop(self.pq)
            if dist != self.distTo[v]: # this is the workaround for no updating value option in heapq
                continue
            for e in G.getAdj(v):
                self.relax(e)

    def relax(self, e):
        v = e.start()
        w = e.end()
        if self.distTo[w] > self.distTo[v] + e.getWeight():
            self.distTo[w] = self.distTo[v] + e.getWeight()
            self.edgeTo[w] = e
            heappush(self.pq, (self.distTo[w], w))
                #  python's heapq doesn't support updating value (i.e. decrease key)
                #  work around: https://algocoding.wordpress.com/2015/03/25/dijkstras-algorithm-part-3a-priority-queue-in-python/
    
    def distTo(self, v):
        return self.distTo[v]

    def hasPathTo(self, v):
        return self.distTo[v] < float('inf')

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        if v == self.s:
            return None
        path = []
        e = self.edgeTo[v]
        while e is not None:
            path.append(e)
            e = self.edgeTo[e.start()]
        return path[::-1]