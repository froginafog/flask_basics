from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index(): 
    return render_template("index.html")

@app.route('/Bob')
def Bob(): 
    return render_template("Bob.html")

@app.route('/Robin')
def Robin(): 
    return render_template("Robin.html")

@app.route('/Mimi')
def Mimi(): 
    return render_template("Mimi.html")

@app.route('/login', methods = ['POST', 'GET'])
def login():
    valid_usernames_passwords = [["Bob", "B000"],
                                 ["Robin", "R000"],
                                 ["Mimi", "M000"]]
    username_password_is_valid = False
    if(request.method == "POST"):
        username_received = request.form['user_name']
        password_received = request.form['pass_word']
        for username_password in valid_usernames_passwords:
            if(username_received == username_password[0] and password_received == username_password[1]):
                username_password_is_valid = True
                break
        if(username_password_is_valid):
            return redirect(url_for(username_received))
        else:
            if(username_received == ""):
                username_received = "_______"
            return render_template("invalid_login.html", username_output = username_received)
    else:
        return render_template("login.html")

if __name__ == '__main__':  
    app.run(debug = True)  





