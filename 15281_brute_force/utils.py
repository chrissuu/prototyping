import itertools
def prod(list_sets):
    '''For set in list_sets, compute the cross product between them'''

    return set(itertools.product(list_sets))

    
