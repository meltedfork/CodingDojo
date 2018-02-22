from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# @app.route('/users/<username>')
# def show_user_profile(username):
#     print username
#     return render_template("user.html")
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
	print username
	print id
    return render_template('user.html')
    
app.run(debug=True)

#<username> matches parameter name passed to route handler function
