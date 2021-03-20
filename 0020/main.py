from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    if(request.method == 'POST'):
        programming_languages_received = request.form;  #the type is dictionary
    return render_template("index.html", programming_languages = programming_languages_received)

if __name__ == '__main__':  
    app.run(debug = True)  





