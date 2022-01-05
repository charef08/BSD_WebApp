import string

# CREATION DE LA TABLE DE L'ALPHABET
alphabet = list(string.ascii_uppercase)

#-------------------------------------------- DECRYPTAGE DE CESAR AVEC CLE --------------------------------------------------------------

# FONCTIONN DE DECALAGE POUR DECRYPTAGE
def decalage_dcr(ltr, dclg):
    i=0
    while i<len(alphabet) and alphabet[i]!=ltr:
        i+=1
    j = i-dclg
    if j < 0:
        j = 25+j+1
    new_ltr = alphabet[j]
    return new_ltr


# FONCTION DE DECRYPTAGE DE CESAR
def decrypter(mot, dcg):
    new_mot=''
    for alp in mot:
        alp2 = decalage_dcr(alp, dcg)
        new_mot = new_mot+alp2
    return new_mot

#-------------------------------------------- DECRYPTAGE DE VIGENERE AVEC CLE --------------------------------------------------------------

# CONVERTION EN CHIFFRE DU CODE DE CRYPTAGE
def code_int(crp_vig0):
    crp_vig1 = []
    for ltr in crp_vig0:
        i=0
        while i<len(alphabet) and alphabet[i]!=ltr:
            i+=1
        crp_vig1.append(str(i))
    return crp_vig1


# FONCTION DE DECRYPTAGE DE VIGENERE
def deCryptage_vg(phrase, cd):
    code = code_int(cd)
    new_mot = ''
    tl = len(code)
    j = 0
    i=0
    while j<len(phrase):
        new_mot += decrypter(phrase[j], int(code[i]))
        i+=1
        j+=1
        if i==tl:
            i=0        
    return new_mot



#-------------------------------------------- DECRYPTAGE DE SUBSTITUTION AVEC CLE --------------------------------------------------------------

# FONCTION DE CRYPTAGE PAR SUBSTITUTION
def decrypt_subt(mot, code):
    # CREATION DU DICTIONNAIRE
    subt ={}
    for i in range(0,26):
        subt[code[i]] = alphabet[i]

    # SUBSTITUTION DES LETTRES 
    mot_crypt = ''
    for ltr in mot:
        mot_crypt += subt[ltr]
    
    return mot_crypt

#-------------------------------------------- CRYPTAGE PAR TRANSPOSITION --------------------------------------------------------------

# FONCTION DE DERYPTAGE PAR TRANSPOSITION
def decrypt_trsp(mot, cle):
    taille = len(mot)
    liste = []
    nbr = taille/cle
    i = 0
    while i<taille:
        part = ''
        for j in range(0, cle):
            part += mot[i]
            i+=1
        liste.append(part)
    
    mot_decrypt = ''
    for j in range(0, cle):
        for elt in liste:
            mot_decrypt += elt[j]
    
    return mot_decrypt.replace('.', '')
    
