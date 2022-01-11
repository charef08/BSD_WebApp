import string

# CREATION DE LA TABLE DE L'ALPHABET
alphabet = list(string.ascii_uppercase)

#-------------------------------------------- CRYPTAGE DE CESAR --------------------------------------------------------------

# #FONCTION DE DECALAGE POUR CRYPTAGE
# def decalage_cr(ltr, dclg):
#     i=0
#     while i<len(alphabet) and alphabet[i]!=ltr:
#         i+=1
#     j = i+dclg
#     if j > 25:
#         j = j-25-1
#     new_ltr = alphabet[j]
#     return new_ltr

#FONCTION DE DECALAGE POUR CRYPTAGE
def decalage_cr(ltr, dclg):
    i=0
    while i<len(alphabet) and alphabet[i]!=ltr:
        i+=1
    j = i+dclg
    if j > 25:
        j = j-25-1
    new_ltr = alphabet[j]
    return new_ltr


# FONCTION DE CRYPTAGE DE CESAR
def crypter(mot, dcg):
    new_mot=''
    for alp in mot:
        alp2 = decalage_cr(alp, dcg)
        new_mot = new_mot+alp2
    return new_mot

#-------------------------------------------- CRYPTAGE DE VIGENERE --------------------------------------------------------------

# CONVERTION EN CHIFFRE DU CODE DE CRYPTAGE
def code_int(crp_vig0):
    crp_vig1 = []
    for ltr in crp_vig0:
        i=0
        while i<len(alphabet) and alphabet[i]!=ltr:
            i+=1
        crp_vig1.append(str(i))
    return crp_vig1


# FONCTION DE CRYPTAGE DE VIGENERE
def Cryptage_vg(phrase, cd):
    phrase=phrase.upper()
    code = code_int(cd)
    new_mot = ''
    tl = len(code)
    j = 0
    i=0
    while j<len(phrase):
        new_mot += crypter(phrase[j], int(code[i]))
        i+=1
        j+=1
        if i==tl:
            i=0        
    return new_mot

# mot2 = Cryptage_vg('cettephraseestunsimpletestdecodage', 'che')
# print(mot2)

#-------------------------------------------- CRYPTAGE PAR SUBSTITUTION --------------------------------------------------------------

code = 'QWERTYUIOPASDFGHJKLZXCVBNM'
mot = 'Cryptographie'.upper()

# FONCTION DE CRYPTAGE PAR SUBSTITUTION
def crypt_subt(mot, code):
    # CREATION DU DICTIONNAIRE
    subt ={}
    for i in range(0,26):
        subt[alphabet[i]] = code[i]

    # SUBSTITUTION DES LETTRES 
    mot_crypt = ''
    for ltr in mot:
        mot_crypt += subt[ltr]
    
    return mot_crypt


#-------------------------------------------- CRYPTAGE PAR TRANSPOSITION --------------------------------------------------------------

# FONCTION DE DECRYPTAGE PAR TRANSPOSITION
def crypt_trsp(mot, cle):
    taille = len(mot)
    liste = []
    i = 0
    while i<taille:
        mott=''
        for j in range(0,cle):
            if i<taille:
                mott+=mot[i]
                i+=1
            else:
                mott+='.'
        liste.append(mott)
    
    mot_crypt = ''
    for i in range(0, cle):
        for j in range(0, len(liste)):
            mot_crypt += liste[j][i]
    
    return mot_crypt



