from flask import Flask, render_template, request, redirect, url_for, session
import json
import urllib
from att_vig import att_vig
from Algos_Cryptage import crypter, crypt_subt, crypt_trsp
from Algo_decryp_cle import decrypter, decrypt_subt, decrypt_trsp
from DES import cryptage_des, decryptage_des
from Algo_cesar import Cryptage_vg, deCryptage_vg
from handler import validate_encrypt_request
import netifaces
import requests

def get_gatway_ip():
    try:
            gateways = netifaces.gateways()
            defaults = gateways.get("default")
            return defaults[2][0]
    except:
            raise Exception('make sure you are online...')

def req(name,state=False):
        data = {'name':name,'active':True}
        try:
                x = requests.post(f"http://{get_gatway_ip()}:3000/get-peers",json=data)
                # x = requests.post(f"http://10.42.0.1:3000/get-peers",json=data)
                if x.status_code == 200:
                        return x.json()
                else:
                        return {}
        except:
                return {}

def send_data(ip,sender,algo,msg,key):
        data = {"sender": sender ,"algorithm": algo ,"message": msg ,"key": key ,"type": "encrypt"}
        url = f'http://{ip}:3000/encrypt'
        try:
                x = requests.post(url, json=data)
                return x.status_code
        except:
                return -1


app = Flask(__name__)

list_msg = []
list_s = req('charef', True)

@app.route('/', methods=['GET', 'POST'])
def index(msg='', cle='', res=''):
    return render_template('index2.html',message=msg, cle=cle, resultat=res)

@app.route('/vigenere', methods=['GET', 'POST'])
def vig(msg='', lk='', val=''): 
    return render_template('vig.html', message=msg, lk=lk, resultat=val)

@app.route('/send', methods=['POST', 'GET'])
def send_page():
    return render_template('send.html')

@app.route('/receive', methods=['POST', 'GET'])
def receive_page(name='', msg='', key='', algo=''):
    try : 
        return render_template('receive.html', name=name, message=msg, key=key, algo=algo)
    except Exception as e:
        print(e)
        
@app.route('/send_message', methods=['POST', 'GET'])
def send_message():
    name = 'charef'
    algo = request.form['algo']
    msg = request.form['msg']
    ip = request.form['adress']
    key = request.form['key']

    send_data(ip, name, algo, msg, int(key))

    return render_template('send.html')

@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    # data = request.get_json(force = True)
    algo = request.form['algo']
    cle = request.form['key']
    methode = request.form['methode']
    msg_org =  request.form['msg']
    msg = ''.join(filter(str.isalnum, msg_org)).upper()
    cle = ''.join(filter(str.isalnum, cle))
    
    try:
        if methode=='Encrypt':
                if algo=='ceasar':
                    res = crypter(msg, int(cle))
                if algo=='vigenere':
                    res = Cryptage_vg(msg, cle.upper())
                if algo=='substitution':
                    res = crypt_subt(msg, cle.upper())
                if algo=='transposition':
                    res = crypt_trsp(msg, int(cle))
                if algo=='DES':
                    res=cryptage_des(msg, cle)
            
        if methode=='Decrypt':
                if algo=='ceasar':
                    res=decrypter(msg, int(cle))
                if algo=='vigenere':
                    res=deCryptage_vg(msg, cle.upper())
                if algo=='substitution':
                    res=decrypt_subt(msg, cle.upper())
                if algo=='transposition':
                    res=decrypt_trsp(msg_org.upper().replace(' ', ''), int(cle))
                if algo=='DES':
                    res=decryptage_des(msg, cle)
            
        return render_template('index2.html', message=msg_org, cle=cle, resultat=res)

    except Exception as e:
        print(e)
        return '<h1>VEUILLEZ VERIFIER LES INFORMATIONS INTRODUITES</h1>'

@app.route('/process_msg', methods=['GET', 'POST'])
def process_msg():
    try:
        name = request.form['name']
        algo = request.form['algo']
        msg_org =  request.form['message']
        cle = request.form['key']
        msg = ''.join(filter(str.isalnum, msg_org)).upper()
        cle = ''.join(filter(str.isalnum, cle))

        res=''
        if str(algo)=='ceasar':
            res=decrypter(msg, int(cle))
        if str(algo)=='vigenere':
            res=deCryptage_vg(msg, cle.upper())
        if str(algo)=='substitution':
            res=decrypt_subt(msg, cle.upper())
        if str(algo)=='transposition':
            res=decrypt_trsp(msg, int(cle))

        print('res : ', res)
            
        return render_template('receive.html', name=name, message=msg_org, algo=algo, keys=cle, resultat=res)

    except:
        return '<h2>Vous devez d\'abord recevoir un message pour pouvoir le decrypter</h2>'

@app.route('/proc_vige', methods=['GET', 'POST'])
def proc_vige():
    message = request.form['msg']
    cle = request.form['key']
    try:
        res = att_vig(message.upper().replace(' ', ''), int(cle))
        return render_template('vig.html', message=message, lk=cle, resultat=res)
    except:
        return '<h1>VEUILLEZ VERIFIER LES INFORMATIONS INTRODUITES</h1>'

@app.route('/encrypt', methods=['GET','POST'])
def encrypt():
    try:
        requestJson = request.get_json(force=True)
        validate_encrypt_request(requestJson)
        sender = requestJson['sender']
        algo = requestJson['algorithm']
        msg = requestJson['message']
        key = requestJson['key']
        typed = requestJson['type']

        list_msg.append(requestJson)


        return 'message recu'

    except:
        return 'erreur'
    
@app.route('/call_list', methods=['GET', 'POST'])
def call_list():
    try:
        if len(list_msg)!=0:
            sender = list_msg[-1]['sender']
            algo = list_msg[-1]['algorithm']
            msg = list_msg[-1]['message']
            key = list_msg[-1]['key']
            return render_template('receive.html', name=sender, message=msg, key=key, algo=algo)
        else:
            return 'aucun msg recu'
    except:
        return 'error' 

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True, port=3000)
