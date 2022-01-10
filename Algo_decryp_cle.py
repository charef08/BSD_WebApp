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

# FONCTION DE DECRYPTAGE PAR TRANSPOSITION
def decrypt_trsp(mot, cle):
    taille = len(mot)
    liste = []
    nbr = round(taille/cle)
    i=0
    while i<taille:
        mott = ''
        for j in range(0, nbr):
            mott += mot[i]
            i+=1
        liste.append(mott)
    
    mot_decrypt = ''
    for i in range(0, nbr):
        for j in range(0, len(liste)):
            mot_decrypt += liste[j][i]
    
    return mot_decrypt.replace('.', '')



    
