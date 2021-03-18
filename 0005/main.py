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
    #We have to include 'f' at the beginning of the string or else 'username' and 'userid' will not be displayed.
    return output

#When the user puts in the address with the path segment '/admin',
#it gets redirect to the function user() which is associated with the path segment '/user/<user_name>/id/<user_id>'.
@app.route("/admin")
def admin():
    return redirect(url_for("user", user_name = "Admin", user_id = 101))
    #when redirecting to the function user(), we also pass the 'user_name' and the 'user_id'

if __name__ == '__main__':  
    app.run(debug = True)  









