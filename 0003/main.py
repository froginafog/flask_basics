from flask import Flask

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index():
    output = "<h1>Index Page</h1>"
    return output

#on the web browser, type: http://127.0.0.1:5000/user/Bob/id/678
@app.route('/user/<user_name>/id/<user_id>') 
def user(user_name, user_id):
    output = f"Welcome to the home page, {user_name}. Your user id is {user_id}.\n"
    #We have to include 'f' at the beginning of the string or else 'username' and 'userid' will not be displayed.
    return output

if __name__ =='__main__':  
    app.run(debug = True)  









