from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('index.html')


@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    data = request.get_data()
    print('i got this : ', data)
    print('success')
    return render_template('example.html')


if __name__ == '__main__':
	app.run(debug=True)




# letter_freq = {
#     'a':0.07636,
#     'b':0.00901,
#     'c':0.0326,
#     'd':0.03669,
#     'e':0.14715,
#     'f':0.01066,
#     'g':0.00866,
#     'h':0.00737,
#     'i':0.07529,
#     'j':0.00613,
#     'k':0.00074,
#     'l':0.05456,
#     'm':0.02968,
#     'n':0.07095,
#     'o':0.05796,
#     'p':0.02521,
#     'q':0.01362,
#     'r':0.06693,
#     's':0.07948,
#     't':0.07244,
#     'u':0.06311,
#     'v':0.01838,
#     'w':0.00049,
#     'x':0.00427,
#     'y':0.00128,
#     'z':0.00326
# }