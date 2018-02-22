from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'TwistKnob'

@app.route('/')
def index():
    # session.clear()       # must clear session on new test of code
    if "counter" not in session:
        session['counter'] = 0
        print("session counter is at 0")
    else:
        print("session counter is increasing")
        session['counter'] += 1
    
    return render_template('index.html', counter=session['counter'])

app.run(debug=True)     

    