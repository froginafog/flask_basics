from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    programming_languages_received = []
    if(request.method == 'POST'):
        programming_languages_received.append(request.form['first_programming_language'])
        programming_languages_received.append(request.form['second_programming_language'])
        programming_languages_received.append(request.form['third_programming_language'])
    return render_template("index.html", programming_languages = programming_languages_received)

if __name__ == '__main__':  
    app.run(debug = True)  





