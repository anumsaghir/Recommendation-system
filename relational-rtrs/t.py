d1 = {121604: {'Eddie Alcazar': 1}, 109064: {'Vietnam War': 1, 'Bill Siegel': 1}, 108043: {'Joey Figueroa': 1, 'too small': 1}, 129036: {'anthropology': 1, 'Anthony Howarth': 1}, 109325: {'climate change': 1}, 112399: {'etaege': 1, 'John Maloof': 1, 'Charlie Siskel': 1, 'BD-R': 1, 'mental illness': 1}}

d2 = {108248: {'Dave Mossop': 1, 'skiing': 1}, 109284: {'America': 1}, 112406: {'Brazil': 1}, 121879: {'Gregg Barson': 1}, 118788: {'Jasmine Dellal': 1}, 120751: {'Paola di Florio': 1}, 111644: {'golf': 1}, 130079: {}, 116002: {'1960s': 1, 'Alison Ellwood': 1}, 113190: {}, 129064: {}, 120873: {}, 128812: {'art': 1, '03/15': 1}}

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

    


