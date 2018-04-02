d1 = {'cool': 2, 'horror': 1, 'terrifying': 2, 'nice movie': 3}

d2 = {'action': 3, 'adventure': 3, 'cool': 1, 'nice movie': 2}

def tags_jaccard_index(d1, d2):
    print('tags--- js')
    set1 = set(d1.keys())
    set2 = set(d2.keys())

    print(set1)
    print(set2)

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    Tag_S = intersection_cardinality/float(union_cardinality)
    
    print(Tag_S)
    
    return(Tag_S)
   
tags_jaccard_index(d1, d2)

    


