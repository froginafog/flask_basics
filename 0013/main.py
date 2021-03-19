from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", programming_languages_output = programming_languages)

if __name__ == '__main__':  
    app.run(debug = True)  

programming_languages = ["C", "C++", "Java", "Python", "Javascript", "PHP"]



