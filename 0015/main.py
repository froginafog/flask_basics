from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    programming_language_received = ""
    if(request.method == 'POST'):
        programming_language_received = request.form['programming_language']
    return render_template("index.html", programming_language = programming_language_received)

if __name__ == '__main__':  
    app.run(debug = True)  





