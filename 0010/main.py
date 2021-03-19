from flask import Flask, render_template, redirect, url_for

app = Flask(__name__) 

@app.route('/')
@app.route('/index')
def index(): 
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/student')
def student():
    return render_template("student.html")

@app.route('/teacher')
def teacher():
    return render_template("teacher.html")

@app.route('/invalid_user')
def invalid_user():
    return render_template("invalid_user.html")


#http://127.0.0.1:5000/user/enter_username_here
@app.route('/user/<username>')
def user(username):
    if username == 'admin':
        return redirect(url_for('admin')) #calls the function admin()
    elif username == 'student':
        return redirect(url_for('student')) #calls the function student()
    elif username == 'teacher':
        return redirect(url_for('teacher')) #calls the function teacher()
    else:
        return redirect(url_for('invalid_user')) #call the function invalid_user()

if __name__ == '__main__':  
    app.run(debug = True)  





