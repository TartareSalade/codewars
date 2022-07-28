import doctest

def XO(s):
    """
    Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
    Return : True or False
    >>> XO("ooxx")
    True
    >>> XO("xooxx")
    False
    >>> XO("ooxXm")
    True
    >>> XO("zpzpzpp")
    True
    >>> XO("zzoo")
    False
    """
    countO = 0
    countX = 0
    for i in s.lower():
        if i == "x":
            countX += 1
        if i == "o":
            countO += 1
    if countO == countX:
        return True
    elif countO == 0 and countX ==0:
        return True
    else:
        return False

doctest.testmod(verbose=False)



