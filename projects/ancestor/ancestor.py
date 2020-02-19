##When I'm done I want to try using a full graph class for more practice
#All my tests are passing...but they won't if I take on harder graphs....because I'm not resetting current & ancestor_paths like I meant to...they should reset every new path...and ancestor_ath should be a list of different-length paths. Not sure what happened there.

from util import Queue, Stack 

################
## USING AN EDGE LIST


# def get_parents(child, family_tree):
#     parents = []
#     for i in family_tree:
#         if child == i[1]:
#             print("Parent found: ", i[0])
#             parents.append(i[0])
#     return parents


# def earliest_ancestor(ancestors, starting_node):
#     #First step...set the graph & relationships in a list/dictionary I can work with

#     #Need a variable storing the chains of ancestry....my answer will be the longest chain's last element?
#     current_path = []
#     ancestor_paths = []

#     #### DEPTH FIRST TRAVERSAL
#     # Create a new Stack
#     s = Stack()
#     # add starting node to queue
#     s.push(starting_node)
#     # create an empty set to store 'visited' nodes
#     visited = set()

#     # While the stack's not empty:
#     while s.size() > 0:

#         #pop the first node
#         a = s.pop()

#         # if node is not in visited
#         if a not in visited:
#             # mark node as visited
#             visited.add(a)
#             # add node to current_path
#             current_path.append(a)

#             # add node's parents to the stack
#             for parents in get_parents(a, ancestors):
#                 s.push(parents)

#     # add current_path to ancestor_paths
#     ancestor_paths.append(current_path)
#     # reset current_path
#     current_path = []

#     # as long as ancestor_paths isn't length of 1 and directed back to itself...
#     if len(ancestor_paths) > 1 or len(ancestor_paths[0]) != 1:
#         # return the last element of the longest ancestor_chain
#         longest = []
#         #return the last element in the longest chain in ancestor_paths
#         for i in ancestor_paths:
#             if len(i) > len(longest):
#                 longest = i
#         return longest[-1]
#     else: 
#          return -1




################
## USING AN ADJACENCY LIST


class Graph():
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            return "Sorry this vertex is already created"

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return "You have to add that vertex"

    def get_children(self, vertex):
        return self.vertices[vertex]

    def get_parents(self, vertex):
        parents = []
        for parent, child in self.vertices.items():
            if vertex in child :
                parents.append(parent)
        return parents

    def dft_longest(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        current_path = []
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print("Visiting: ", v)
                current_path.append(v)
                visited.add(v)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_parents(v):
                    s.push(neighbor)
        return current_path


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    for i in ancestors:
        g.add_edges(i[0], i[1])
    # print("Here's your graph: ", g.vertices)

    parents = g.get_parents(starting_node)
    print("Parents: ", parents)

    ## ok my get_parents function works...just gotta use DFS and trace it up the right way!
    res = g.dft_longest(starting_node)
    print(res)
    if len(res) > 1 or res[0] != starting_node:
        return res[-1]
    else:
        return -1