"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

import math

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        """Add edge from v1 to v2."""        
        # If they're both in the graph
        if v1 in self.vertices and v2 in self.vertices:
        	self.vertices[v1].add(v2)        
        else:
        	raise IndexError("Vertex does not exist in graph")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        """Breadth-first Traversal."""        
        q = Queue()
        q.enqueue(starting_vertex)        
        # Keep track of visited nodes
        visited = set()        
        # Repeat until queue is empty
        while q.size() > 0:
        	
        	# Dequeue first vert
        	v = q.dequeue()        
        	# If it's not visited:
        	if v not in visited:
                 print(v)             
                 # Mark visited
                 visited.add(v)        
                 for next_vert in self.get_neighbors(v):
                      q.enqueue(next_vert)        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:

            v = s.pop()

            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visitted = set()

        def inner(v):
            if v not in visitted:
                 print(v)
                 visitted.add(v)
     
                 for next_vert in self.get_neighbors(v):
                     inner(next_vert)
        

        inner(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        visitted = set()
        
        path = {}
        for i, v in self.vertices.items():
            if i == starting_vertex:
                path[i] = [0, None]
            else:
                path[i] = [math.inf, None] 

        while q.size() > 0:
            v = q.dequeue()
            if v not in visitted:
                visitted.add(v)
       
                for nxt_v in self.get_neighbors(v):
                    q.enqueue(nxt_v)

                    d = path[v][0] + 1
                    s_d = path[nxt_v][0]
                    if d < s_d:
                        path[nxt_v]=[d, v]

        result=[]
        d_v = destination_vertex
        while d_v:
            result.insert(0, d_v)
            d_v = path[d_v][1]
        return result
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        path = {}
        for i, v in self.vertices.items():
            if i == starting_vertex:
                path[i] = [0, None]
            else:
                path[i] = [math.inf, None] 

        while s.size() > 0:

            v = s.pop()

            if v not in visited:
                
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

                    d = path[v][0] + 1
                    s_d = path[next_vert][0]
                    if d < s_d:
                        path[next_vert]=[d, v]

        result=[]
        d_v = destination_vertex
        while d_v:
            result.insert(0, d_v)
            d_v = path[d_v][1]
        return result

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
