
# (1,3),(2,3),(3,6),(5,6),(5,7),(4,5),(4,8),(8,9),(11,8),(10,1) && 6
#returns 10

#loop through tuples and find all pairs that have the starting_node as a child

#if there is a pair or pairs save those and then repeat step 1 but with the parent
#of starting_node as a child

#repeat step 2 until the ealiest ancestor is found

def find_pairs(ancestors, children):
    new_pairs = []

    for child in children:
        for pc_pair in ancestors:
            if pc_pair[1] == child:
                new_pairs.append(pc_pair[0])

    if len(new_pairs) < 1:
        return children
    else:
        return new_pairs


def earliest_ancestor(ancestors, starting_node):
    generation = 0
    starting_node = [starting_node]
    searching = True
    ealiest = None
    
    while searching:
        pairs_list = find_pairs(ancestors, starting_node)
        #if there is not a ealier ancestor
        if generation == 0 and starting_node == pairs_list:
            searching = False
            ealiest = -1
        #if find_paris returns the same thing we put into it
        elif starting_node == pairs_list:
            searching = False
            ealiest = min(pairs_list)
        #if we found new parents
        else:
            generation += 1
            starting_node = pairs_list

    return ealiest


#3  5
#1  2  4
#10

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors, 9))
print(earliest_ancestor(test_ancestors, 7))

