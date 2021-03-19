from flask import Flask, render_template

app = Flask(__name__) 

#url example: http://127.0.0.1:5000/index/user/Bob/id/567
@app.route('/index/user/<user_name>/id/<user_id>')
def index(user_name, user_id): 
    return render_template("index.html", user_name_output = user_name, user_id_output = user_id)

if __name__ == '__main__':  
    app.run(debug = True)  





