from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  print "Things are working"
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print "working here too"
    print request.form
    context = {
      'name': request.form['name'],
      'location': request.form['location'],
      'language': request.form['language'],
      'comment': request.form['comment']
    }  
    return render_template("result.html", **context)
  
app.run(debug=True)  