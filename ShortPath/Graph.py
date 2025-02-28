# Sebastian Cardona
import math
import heapq


class Graph:
    def _buildEncoding(self):
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index = index + 1

    def _buildAdjList(self):
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append((relation[1], relation[2]))

    def _buildRelation(self, e):
        if self.directed:
            self.relations = e
        else:
            self.relations = set()
            for el in e:
                self.relations.add(el)
                self.relations.add((el[1], el[0], el[2]))

    def __init__(self, v, e, directed=True):
        self.directed = directed
        self.vertexes = v
        self._buildRelation(e)
        self._buildAdjList()
        self._buildEncoding()

    def getAdjList(self):
        return self.adjList

    def _buildVProps(self, source=None):
        self.v_props = {}
        for v in self.vertexes:
            self.v_props[v] = {"distance": math.inf, "parent": None}
        if source is not None:
            self.v_props[source] = {"distance": 0, "parent": None}

    def _getNeighborsAdjList(self, vertex):
        return self.adjList[vertex]

    def getNeighbors(self, vertex):
        return self._getNeighborsAdjList(vertex)

    def dijkstra(self, source):
        if source not in self.vertexes: # O(1)
            raise ValueError("Vertex not in graph")
        self._buildVProps(source) # O(V)
        priority_queue = [(0, source)] # O(1)
        while priority_queue: # O(V)
            current_distance, u = heapq.heappop(priority_queue) # O(log(V))
            if current_distance > self.v_props[u]["distance"]: # O(1)
                continue
            for neighbor, weight in self.getNeighbors(u): # O(E)
                distance = self.v_props[u]["distance"] + weight # O(1)
                if distance < self.v_props[neighbor]["distance"]: # O(1)
                    self.v_props[neighbor]["distance"] = distance # O(1)
                    self.v_props[neighbor]["parent"] = u # O(1)
                    heapq.heappush(priority_queue, (distance, neighbor)) # O(log(V))
        return self.v_props

    # O(dijkstra) = O(V + log(V)(V + E)) = O((V + E)log(V))

    def floyd_warshall(self):
        dist = {v: {w: math.inf for w in self.vertexes} for v in self.vertexes} # O(V^2)
        for v in self.vertexes: # O(V)
            dist[v][v] = 0 # O(1)
        for u in self.adjList: # O(V)
            for v, weight in self.adjList[u]: # O(E)
                dist[u][v] = weight # O(1)
        for k in self.vertexes: # O(V)
            for i in self.vertexes: # O(V)
                for j in self.vertexes: # O(V)
                    if dist[i][j] > dist[i][k] + dist[k][j]: # O(1)
                        dist[i][j] = dist[i][k] + dist[k][j] # O(1)
        return dist

    # O(floyd_warshall) = O(V^2 + V * V * V) = O(V^3)

    def bellman_ford(self, source):
        if source not in self.vertexes: # O(1)
            raise ValueError("Vertex not in graph")
        self._buildVProps(source) # O(V)
        for _ in range(len(self.vertexes) - 1): # O(V)
            for u in self.adjList: # O(V)
                for v, weight in self.adjList[u]: # O(E)
                    if (
                        self.v_props[u]["distance"] + weight
                        < self.v_props[v]["distance"]
                    ): # O(1)
                        self.v_props[v]["distance"] = (
                            self.v_props[u]["distance"] + weight
                        ) # O(1)
                        self.v_props[v]["parent"] = u # O(1)
        for u in self.adjList: # O(V)
            for v, weight in self.adjList[u]: # O(E)
                if (self.v_props[u]["distance"] + weight <
                        self.v_props[v]["distance"]):
                    raise ValueError(
                        f"Graph with negative cycle in {u} to {v}"
                    )
        return self.v_props

    # O(bellman_ford) = O(V + V * E) = O(V * E)
