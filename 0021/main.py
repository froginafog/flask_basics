from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    if(request.method == 'POST'):
        x_data.append(request.form['x_input'])
        y_data.append(request.form['y_input'])
    table_values = zip(x_data, y_data) # zip() returns an iterator of tuples 
    return render_template("index.html", table_values_output = table_values)

if __name__ == '__main__':  
    app.run(debug = True)  

x_data = []
y_data = []



