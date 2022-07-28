def ocurrence_lettres(txt):
    """
    Objectif : Compter le nbr de lettres dans une chaine de caractère grâce à un dictionnaire
    Paramètres : Chaine de caractère
    Returns : Renvoie un dictionnaire contenant chaque lettre avec le nbr de fois ou elle apparait 
    """
    nbr_occurences = {} #On mets en place un dictionnaire car on renvoie un dictionnaire
    for k in txt: #On parcours la chaine de caractère, chaque lettre
        for i in k:
            if i in nbr_occurences:
                nbr_occurences[i.lower()] += 1 #Enlever le .lower() si on veut faire en sorte que les maj / min soit des caractères diff
            else:
                nbr_occurences[i.lower()] = 1 #Enlever le .lower() si on veut faire en sorte que les maj / min soit des caractères diff
    return nbr_occurences

print(ocurrence_lettres("tagAda"))