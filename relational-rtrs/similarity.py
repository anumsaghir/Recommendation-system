"""
Calculate similarity between two things (strings, lists, etc)
"""


def jaccard_index(s1, s2):
    set1 = set(s1.split(' '))
    set2 = set(s2.split(' '))

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    return intersection_cardinality/float(union_cardinality)


def genres_jaccard_index(s1, s2):
    set1 = set(s1.split('|'))
    set2 = set(s2.split('|'))

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    return intersection_cardinality/float(union_cardinality)

def tags_jaccard_index(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    return intersection_cardinality/float(union_cardinality)
