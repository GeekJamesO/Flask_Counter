from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def root():
    try:
        session['counter'] += 1
    except Exception as e:
        session['counter'] = 1
    return render_template('Counter.html', counter=session['counter'])

@app.route('/plusTwo')
def plusTwo():
    try:
        session['counter'] += 1
    except Exception as e:
        session['counter'] = 1
    return redirect('/')

@app.route('/reset')
def reset():
        session['counter'] = 0
        return redirect('/')

app.run(debug=True)
