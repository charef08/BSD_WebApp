import string
import itertools



# CREATION DE LA TABLE DE L'ALPHABET
alphabet = list(string.ascii_uppercase)

# CONVERTION EN CHIFFRE DU CODE DE CRYPTAGE
def code_int(crp_vig0):
    crp_vig1 = []
    for ltr in crp_vig0:
        i=0
        while i<len(alphabet) and alphabet[i]!=ltr:
            i+=1
        crp_vig1.append(str(i))
    return crp_vig1


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

letter_freq = {
  'a':0.07636,
  'b':0.00901,
  'c':0.0326,
  'd':0.03669,
  'e':0.14715,
  'f':0.01066,
  'g':0.00866,
  'h':0.00737,
  'i':0.07529,
  'j':0.00613,
  'k':0.00074,
  'l':0.05456,
  'm':0.02968,
  'n':0.07095,
  'o':0.05796,
  'p':0.02521,
  'q':0.01362,
  'r':0.06693,
  's':0.07948,
  't':0.07244,
  'u':0.06311,
  'v':0.01838,
  'w':0.00049,
  'x':0.00427,
  'y':0.00128,
  'z':0.00326
}

def att_vig(txt, lenk):

    depth = 3

    lettre_cle = []

    blocs = []
    i = 0

    for i in range(lenk):
        j = i
        t = ''
        while j<len(txt):
            t += txt[j]
            j+=lenk

        blocs.append(t)



    for bloc in blocs:
            
        dict_alp = {}
        for lettre in alphabet:
            dict_alp[lettre] = 0
            
        for lettre in bloc:
            dict_alp[lettre] +=1
        

        dict_alp_2 = {}
        for lettre in dict_alp.keys():
            dict_alp_2[lettre] = float(dict_alp[lettre]/len(bloc))
        

        point_lettre = []
        for i in range(0, 26):
            point_final = 0
            lettre = chr(i+97).upper()
            for j in range(0, 26):
                point_freq = letter_freq[chr(j+97)]
                lettre_moy = chr(((i+j)%26)+97).upper()
                point_norm = dict_alp_2[lettre_moy]
                point_final += point_freq*point_norm
            point_lettre.append((lettre, point_final))
        
        # print(point_lettre)
        point_lettre.sort(key=lambda tup: tup[1], reverse=True)
        # print(point_lettre)

        best_lettre=[]
        for lettre in point_lettre[:depth]:
            best_lettre.append(lettre[0])
        
        lettre_cle.append(best_lettre)
    
    list_cle = []
    for indexes in itertools.product(range(depth), repeat=lenk):
        optioncle = ''
        for i in range(lenk):
            optioncle += lettre_cle[i][indexes[i]]
        list_cle.append(optioncle)


    txt_claire = {}
    for cle in list_cle:
        cle = cle.upper()
        txt_claire[cle] = deCryptage_vg(txt, cle)
    
    return txt_claire

    
    





# txt = 'bapapidiepvipvqcfxpowdrvcznmfjmnebvslspmpiqscqeiqaxwgvcifmaxgfkknxgopivrqiscnpgdgvgmdieigmmnfihxpeuxrvqopvrwcnrthwbenisslcvqbrbepdbmbeulbrleganzmttmqiqtkvnxgop'
# att_vig(txt.upper(), 6)

# txt = 'SDHRFLHFWESEGPGZIEWWGDCYHFBPOTRPDCSNWPIDSOOYGWSDXPIIZPGXOEVDZPGPBTUXSDZPGRSZQLQSSDSEZPGAFZPWSXSDOCSDCFRCSLIBIZHTRTSY'
# att_vig(txt.upper(), 2)


    