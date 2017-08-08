from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except Exception as e:
        session['counter'] = 1
    return render_template('Counter.html')

@app.route('/plusTwo', methods=['GET','POST'])
def plusTwo():
    try:
        session['counter'] += 1
    except Exception as e:
        session['counter'] = 1
    return redirect('/')

@app.route('/reset', methods=['GET','POST'])
def reset():
        session['counter'] = 0
        return redirect('/')

app.run(debug=True)
