from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = 'TwistKnob'

def get_random(): # Set session:
    print 'this is get_random method'
    session['number_ans'] = random.randrange(0, 101)
    print session['number_ans']

@app.route('/')
def number_game():
    if 'number_ans' not in session:
        get_random()
    print "Things are working" 
    return render_template('index.html')

@app.route('/process', methods=['POST']) 
def process():
    guess = request.form['guess']
    if int(request.form['guess']) > session['number_ans']:
        result = 'too high' 
    elif int(request.form['guess']) < session['number_ans']:
        result = 'too low'
    elif int(request.form['guess']) == session['number_ans']:
        result = 'you won!', 'the number was ', session['number_ans']
    else:
        result = 'play by the rules, man'
    
    return render_template('index.html', guess = guess, result = result)

@app.route('/reset') # If want to play again, Remove number from session
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)   