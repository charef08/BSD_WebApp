import string

# CREATION DE LA TABLE DE L'ALPHABET
alphabet = list(string.ascii_uppercase)
# print(alphabet) # AFFICHAGE DE L'ALPHABET

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


# FONCTION DE CRYPTAGE DE CESAR
def crypter(mot, dcg):
    new_mot=''
    for alp in mot:
        alp2 = decalage_cr(alp, dcg)
        new_mot = new_mot+alp2
    return new_mot


# FONCTION DE DECRYPTAGE DE CESAR
def decrypter(mot, dcg):
    new_mot=''
    for alp in mot:
        alp2 = decalage_dcr(alp, dcg)
        new_mot = new_mot+alp2
    return new_mot

# LECTURE DE LA PHRASE 
# phrase = str(input('Donner un mot a crypter : \n')).upper().replace(' ', '')

# LECTURE DU NOMBRE DE DECALAGE 
# dcg = int(input('Donner le nombre de decalage : \n'))

# TEST ET AFFICHAGE DU CRYPTAGE ET DECRYPTAGE DE CESAR
# mot2 = crypter(phrase, dcg)
# mot3 = decrypter(mot2, dcg)
# print(mot2)
# print(mot3)


print('------------------------------------------------------------------------------')

# LECTURE DU CODE DE CRYPTAGE DE VIGENERE
# crp_vig0 = str(input('Donner le code de cryptage : \n')).upper().replace(' ', '')

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

# phrase='JESUISALMAISON'
# crp_vig0='c'
# TEST ET AFFICHAGE DU CRYPTAGE ET DECRYPTAGE DE VIGENERE
# mof = Cryptage_vg(phrase, crp_vig0)
# print(mof)
# mof2 = deCryptage_vg(mof, crp_vig0)
# print(mof2)


        



