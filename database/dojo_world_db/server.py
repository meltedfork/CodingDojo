from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'world'

print 'something is happening'

@app.route('/')
def get_country():
    cursor = mysql.connection.cursor()
    print "Things are working" 
    cursor.execute("SELECT countries.name FROM countries")
    countries = cursor.fetchall()
    return render_template('index.html', countries = countries)

if __name__ == "__main__":
    app.run(debug=True)