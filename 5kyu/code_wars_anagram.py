def anagrams(word, words):
    """
    Deux mots sont des anagrames si l'un et l'autre contiennent les mêmes lettres
    """
    d = {}
    for i in words:
        for k in i:
            if k in d:
                d[k] = d[k] +1
            else:
                d[k] = 1
    return d

















print(anagrams("niche", ["niche", "fdp"]))