from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninjas')
def show_info():
  return render_template("ninjas.html")

@app.route('/dojos/new', methods=['GET', 'POST'])
def new_user():
  if request.method == 'POST':
    name = request.form['name']
    contact = request.form['contact']
    print request.form
    return redirect('/')
  else:
    return render_template("dojos.html")

app.run(debug=True)

