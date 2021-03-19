from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", A_output = A, column_names_output = column_names)

if __name__ == '__main__':  
    app.run(debug = True)  

A = [["A_1_1", "A_1_2", "A_1_3"],
     ["A_2_1", "A_2_2", "A_2_3"],
     ["A_3_1", "A_3_2", "A_3_3"]]
column_names = ["column 1", "column 2", "column3"]



