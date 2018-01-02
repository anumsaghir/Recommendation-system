def search4vowels(word):
    """ Return sny vowels founded in  a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    #return found
    for vowels in found:
        print(vowels)
