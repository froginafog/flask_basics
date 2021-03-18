from flask import Flask, redirect, url_for

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index():
    output = "<h1>Index Page</h1>"
    return output

@app.route('/user/<user_name>/id/<user_id>')
def user(user_name, user_id):
    output = f"Welcome to the home page, {user_name}. Your user id is {user_id}.\n"
    #We have to include 'f' at the beginning of the string or else 'user_name' and 'user_id' will not be displayed.
    return output

#When the user puts in the address with the path segment '/admin',
#it gets redirect to the function index() which is associated with the path segment '/index'.
@app.route("/admin")
def admin():
    return redirect(url_for("index")) 

if __name__ =='__main__':  
    app.run(debug = True)  









