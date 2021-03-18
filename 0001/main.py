from flask import Flask

app = Flask(__name__) 

@app.route('/home/<visitor_name>')
def home(visitor_name): #http://127.0.0.1:5000/home/enter_name_here
    output = "Welcome to the home page, %s."% visitor_name 
    return output

if __name__ =='__main__':  
    app.run(debug = True)  









