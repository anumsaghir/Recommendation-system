d1 = {'cool': 2, 'horror': 1, 'terrifying': 2, 'nice movie': 3}

d2 = {'action': 3, 'adventure': 3, 'cool': 1, 'nice movie': 2}

def tags_jaccard_index(d1, d2):
    print('tags--- js')
    set1 = set(d1.keys())
    set2 = set(d2.keys())

    print(set1)
    print(set2)

    common_tags = set.intersection(set1, set2)
    common_tags_count = 0
    all_tags_count = sum(d1.values()) + sum(d2.values())

    for k, v in d1.items():
        if k in common_tags:
            common_tags_count += v

    for k, v in d2.items():
        if k in common_tags:
            common_tags_count += v

    # print(common_tags_count)
    # print(all_tags_count)

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    Tag_S = intersection_cardinality/float(union_cardinality)
    
    # print(Tag_S)
    
    final_tag_similarity = ((common_tags_count / all_tags_count) * 10) * Tag_S
    
    return(final_tag_similarity)
   
print(tags_jaccard_index(d1, d2))
