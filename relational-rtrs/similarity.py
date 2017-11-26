"""
Calculate similarity between two things (strings, lists, etc)
"""


def jaccard_index(s1, s2):
    set1 = set(s1.split(' '))
    set2 = set(s2.split(' '))

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    return intersection_cardinality/float(union_cardinality)
