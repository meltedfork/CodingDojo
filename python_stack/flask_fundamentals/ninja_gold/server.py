from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = 'TwistKnob'

@app.route('/')
def index():    
    print 'Things are working'
    gold = 0
    return render_template('index.html')


@app.route('/process', methods=['POST'])    
def process():
    print '/process is working'
    # if click ('Find Gold' submit button) then
    # 
    print request.form



@app.route('/display')
def display():
    # to display new gold amount and all activity



@app.route('/reset') # If want to play again, Remove number from session
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)   
