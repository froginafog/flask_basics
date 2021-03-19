from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/Bob')
def Bob():
    return render_template("Bob.html")

@app.route('/login', methods = ['POST'])  
def login():
    if(request.method == "POST"):
        username_received = request.form["user_name"]
        if(username_received == "Bob"):
            return redirect(url_for("Bob"))
        else:
            return render_template("invalid_username.html", username_output = username_received)
    else:
        return render_template("login.html")

if __name__ == '__main__':  
    app.run(debug = True)  





