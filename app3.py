from flask import * 
from flask_mysqldb import MySQL
# pip install flask-mysqldb
app = Flask ("myflaskWithSQL")
app.secret_key = "abcd" # to create session variables you need this key

#database connection
app.config['MYSQL_HOST'] = '192.168.1.141'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'Samid@2013'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def Home():
    cur= mysql.connection.cursor()
    cur.execute("SELECT * FROM movie_details")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('getall.html', data=fetchdata)

@app.route('/insert', methods=["POST"])
def insert():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO movie_details (name, description) VALUES (%s, %s)", (name, description))
        mysql.connection.commit()
        cur.close()
        flash("Data Inserted Successfully")
    return redirect(url_for('Home'))

@app.route('/form')
def form():
    return render_template('form.html')  # Render the form

@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        query = request.form['query']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM movie_details WHERE name LIKE %s", ('%' + query + '%',))
        search_results = cur.fetchall()
        cur.close()
    return render_template('search_results.html', data=search_results, query=query)
    

@app.route('/remove')
def remove():
    return render_template('delete.html')  # Render the delete page

@app.route('/delete', methods=["POST"])
def delete():
    if request.method=="POST":
        name = request.form['name']
        cur = mysql.connection.cursor()
        cur.execute("delete FROM movie_details WHERE name LIKE %s", ('%' + name + '%',))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('Home'))  
app.run(debug=True)