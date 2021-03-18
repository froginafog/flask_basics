from flask import Flask

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index():
    output = "<h1>Index Page</h1>"
    return output

@app.route('/home/user/<string:username>/id/<int:userid>')
def home(username, userid): #http://127.0.0.1:5000/home/user/enter_user_name_here/enter_user_id_here
    output = "Welcome to the home page, %s. Your user id is %d.\n" % (username, userid) 
    return output

if __name__ =='__main__':  
    app.run(debug = True)  









