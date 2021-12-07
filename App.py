from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    Algo = request.form['algo']
    methode = request.form['methode']
    key = request.key['key']
    return 'algo : '+ algo+'methode : '+methode 


if __name__ == '__main__':
	app.run(debug=True)