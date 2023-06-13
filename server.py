from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def template():
    if 'visits' in session:
        session['visits'] +=1
    if 'number' in session:
        session['number']+=1
    else:
        session['visits'] = 0
        session['number'] = 0
    return render_template('index.html')

@app.route('/count')
def counter():
    session['number']+=1
    return redirect('/')

@app.route('/add_two')
def itterate_twice():
    session['number']+=1
    return redirect('/')

@app.route('/user_input', methods=['POST'])
def user_input():
    session['number'] += int(request.form['form'])-1
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)