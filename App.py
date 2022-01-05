from flask import Flask, render_template, request, redirect, url_for, session
import json
import urllib
from att_vig import att_vig
from Algos_Cryptage import crypter, crypt_subt
from Algo_decryp_cle import decrypter, decrypt_subt, decrypt_trsp
from DES import cryptage_des, decryptage_des
from Algo_cesar import Cryptage_vg, deCryptage_vg
# from package.server.base.app import app





app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(msg='', cle='', res=''): 
    return render_template('index2.html',message=msg, cle=cle, resultat=res)

@app.route('/vigenere', methods=['GET', 'POST'])
def vig(msg='', lk='', val=''): 
    return render_template('vig.html', message=msg, lk=lk, resultat=val)



@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    # data = request.get_json(force = True)
    algo = request.form['algo']
    cle = request.form['key']
    methode = request.form['methode']
    msg = request.form['msg'].upper().replace(' ', '')
    
    try:
        if methode=='Encrypt':
                if algo=='Cesar':
                    res = crypter(msg, int(cle))
                if algo=='Vigenere':
                    res = Cryptage_vg(msg, cle.upper())
                if algo=='Substitution':
                    res = crypt_subt(cle.upper(), msg)
                if algo=='Transposition':
                    print(1)
                if algo=='DES':
                    res=cryptage_des(msg, cle)
            
        if methode=='Decrypt':
                if algo=='Cesar':
                    res=decrypter(msg, int(cle))
                if algo=='Vigenere':
                    res=deCryptage_vg(msg, cle.upper())
                if algo=='Substitution':
                    res=decrypt_subt(cle.upper(), msg)
                if algo=='Transposition':
                    res=decrypt_trsp(msg, int(cle))
                if algo=='DES':
                    res=decryptage_des(msg, cle)
            
        return render_template('index2.html', message=msg, cle=cle, resultat=res)

    except:
        return '<h1>VEUILLEZ VERIFIER LES INFORMATIONS INTRODUITES</h1>'


@app.route('/proc_vige', methods=['GET', 'POST'])
def proc_vige():
    message = request.form['msg']
    cle = request.form['key']
    try:
        res = att_vig(message.upper().replace(' ', ''), int(cle))
        return render_template('vig.html', message=message, lk=cle, resultat=res)
    except:
        return '<h1>VEUILLEZ VERIFIER LES INFORMATIONS INTRODUITES</h1>'




if __name__ == '__main__':
	app.run(debug=True, port=3000)
