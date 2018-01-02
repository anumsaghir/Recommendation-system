def search4vowels(phrase: str) -> set:
    """ Return any vowels founded in  a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
    #for vowels in found:
     #   print(vowels)
     
     
def search4letters(phrase: str, letters:str='aeiou') -> set:
    """ Return a set of letters found in  a supplied phrase."""
    return set(letters).intersection(set(phrase))
