from flask import Flask, render_template, url_for 
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def team():
    image_path = url_for('static', filename='img/tmnt.png')
    return render_template('ninja.html', image_path=image_path)

@app.route('/ninja/<color>')
def team_member(color):
    print color
    if color == 'red' or color == 'blue' or color == 'purple' or color == 'orange':   
        image_path = url_for('static', filename='img/'+color+'.jpg')
    else:
        image_path = url_for('static', filename='img/notapril.jpg')    
    return render_template('ninja.html', image_path=image_path)
app.run(debug=True)  

# next time refactor to have img dict