"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    
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
        # Create an empty queue and enqueue the starting_vertex
        the_queue = []
        the_queue.append(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while len(the_queue) > 0:
            # get current vertex (dequeue from queue)
            cur_vertex = the_queue[0]
            the_queue.pop(0)
            # Check if the current vertex has not been visited:
            if cur_vertex not in visited:
                # print the current vertex
                print(cur_vertex)
                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited.add(cur_vertex)
                # queue up all the current vertex's neighbors (so we can visit them next)
                for el in self.vertices[cur_vertex]:
                    the_queue.append(el)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex 
        the_stack = []
        the_stack.append(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the stack is not empty:
        while len(the_stack) > 0:
            # get current vertex (pop from stack)
            cur_vertex = the_stack[0]
            the_stack.pop(0)
            # Check if the current vertex has not been visited:
            if cur_vertex not in visited:
                # print the current vertex
                print(cur_vertex)
                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited.add(cur_vertex)
                # push up all the current vertex's neighbors (so we can visit them next
                for el in self.vertices[cur_vertex]:
                    the_stack.insert(0, el)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        #base case: if the el is not in visited print the el
        if starting_vertex not in visited:
            print(starting_vertex)
            #add to visited
            visited.add(starting_vertex)
            #call on neighbors
            for el in self.vertices[starting_vertex]:
                self.dft_recursive(el, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex 
        the_queue = []
        the_queue.append([starting_vertex])
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while len(the_queue) > 0:
            # get current vertex PATH (dequeue from queue)
            cur_path = the_queue[0]
            the_queue.pop(0)
            # set the current vertex to the LAST element of the PATH
            cur_vertex = cur_path[len(cur_path) - 1]
            # Check if the current vertex has not been visited:
            if cur_vertex not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if cur_vertex == destination_vertex:
                    return cur_path
                # Mark the current vertex as visited
                visited.add(cur_vertex)
                # Add the current vertex to a visited_set
                # Queue up NEW paths with each neighbor:
                for el in self.vertices[cur_vertex]:
                    # take current path
                    # append the neighbor to it
                    # queue up NEW path
                    new_path = list(cur_path)
                    new_path.append(el)
                    the_queue.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and add the PATH TO starting_vertex 
        the_stack = []
        the_stack.append([starting_vertex])
        # Create an empty set to track visited verticies
        visited = set()
        # while the stack is not empty:
        while len(the_stack) > 0:
            # get current vertex PATH
            cur_path = the_stack[0]
            the_stack.pop(0)
            # set the current vertex to the LAST element of the PATH
            cur_vertex = cur_path[len(cur_path) - 1]
            # Check if the current vertex has not been visited:
            if cur_vertex not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if cur_vertex == destination_vertex:
                    return cur_path
                # Mark the current vertex as visited
                visited.add(cur_vertex)
                # Add the current vertex to a visited_set
                # Add the NEW paths with each neighbor:
                for el in self.vertices[cur_vertex]:
                    # take current path
                    # append the neighbor to it
                    # add the NEW path
                    new_path = list(cur_path)
                    new_path.append(el)
                    the_stack.insert(0, new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #add current vertex to visited set and create new updated path
        visited.add(starting_vertex)
        # next_path = list(path)
        # next_path.append(starting_vertex)
        path = path + [starting_vertex]

        #base case: current vertex is the destination
        if starting_vertex == destination_vertex:
            return path

        #loop through the vertices and check path if el not in visited
        for el in self.vertices[starting_vertex]:
            if el not in visited:
                new_path = self.dfs_recursive(el, destination_vertex, path, visited)
                if new_path:
                    return new_path
            else:
                return None


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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
