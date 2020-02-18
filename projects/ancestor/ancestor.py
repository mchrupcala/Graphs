##When I'm done I want to try using a full graph class for more practice

from util import Queue, Stack 

def get_parents(child, family_tree):
    parents = []
    for i in family_tree:
        if child == i[1]:
            print("Parent found: ", i[0])
            parents.append(i[0])
    return parents


def earliest_ancestor(ancestors, starting_node):
    #First step...set the graph & relationships in a list/dictionary I can work with

    #Need a variable storing the chains of ancestry....my answer will be the longest chain's last element?
    current_path = []
    ancestor_paths = []

    #### DEPTH FIRST TRAVERSAL
    # Create a new Stack
    s = Stack()
    # add starting node to queue
    s.push(starting_node)
    # create an empty set to store 'visited' nodes
    visited = set()

    # While the stack's not empty:
    while s.size() > 0:

        #pop the first node
        a = s.pop()

        # if node is not in visited
        if a not in visited:
            # mark node as visited
            visited.add(a)
            # add node to current_path
            current_path.append(a)

            # add node's parents to the stack
            for parents in get_parents(a, ancestors):
                s.push(parents)

    # add current_path to ancestor_paths
    ancestor_paths.append(current_path)
    # reset current_path
    current_path = []

    # as long as ancestor_paths isn't length of 1 and directed back to itself...
    if len(ancestor_paths) > 1 or len(ancestor_paths[0]) != 1:
        # return the last element of the longest ancestor_chain
        longest = []
        #return the last element in the longest chain in ancestor_paths
        for i in ancestor_paths:
            if len(i) > len(longest):
                longest = i
        return longest[-1]
    else: 
         return -1