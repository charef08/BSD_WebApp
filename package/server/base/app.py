from flask import Flask, request
from handler import validate_encrypt_request
from peer_discovery import  request, extract_list_of_users, send_data


app = Flask(__name__)



@app.route('/encrypt', methods=['POST'])
def encrypt():
    requestJson = request.get_json(force=True)
    validate_encrypt_request(requestJson)
    sender = requestJson['sender']
    algorithm = requestJson['algorithm']
    msg = requestJson['message']
    key = requestJson['key']
    typed = requestJson['type']
    
    try:
        if algo=='cesar':
                    res=decrypter(msg, cle)
        if algo=='vigenere':
                    res=deCryptage_vg(msg, cle.upper())
        if algo=='substitution':
                    res=decrypt_subt(cle.upper(), msg)
        if algo=='transposition':
                    res=decrypt_trsp(msg, cle)
            
        return "<h1>Vous avez recu un message :</h1>\
            <p> sender is {{ sender}} <br> \
                algorithm : {{algorithm}} <br> \
                message crypte : {{msg}} <br> \
                message claire : {{res}} <br> \
            </p>"

    except:
        return '<h1>VEUILLEZ VERIFIER LES INFORMATIONS INTRODUITES</h1>'

#  lancer l'application à travers la programmation depuis un autre fichier python
# from app import app
# app.run(port=3000)