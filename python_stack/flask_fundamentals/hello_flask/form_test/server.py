from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/') # our index route will handle rendering our form
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   print request.form
   # redirects back to the '/' route; UPDATE: redirects to '/show' route to go to page that will display info
   return redirect('/show')
@app.route('/show')
def show_user():
  return render_template('user.html')
   
app.run(debug=True) # run our server
