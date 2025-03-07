from flask import * 
import pymysql

app = Flask ("myflaskWithSQL")
app.secret_key = "abcd" # for the flash variable
db_config = {
    'host': '192.168.1.141',
    'user': 'flaskuser',
    'password': 'Samid@2013',
    'database': 'flask'
}

# Function to get a database connection
def get_db_connection():
    connection = pymysql.connect(**db_config)
    return connection

@app.route('/')
def Home():
    connection = get_db_connection() # Step 1: Connect to MySQL
    cursor = connection.cursor() # Step 2: Create a cursor
    cursor.execute("SELECT * FROM movie_details") # Step 3: Execute SQL query
    fetchdata = cursor.fetchall()  # Step 4: Fetch all results
    cursor.close() # Step 5: Close cursor
    connection.close() # Step 6: Close database connection
    return render_template('getall.html', data=fetchdata)

@app.route('/insert', methods=["POST"])
def insert():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO movie_details (name, description) VALUES (%s, %s)", (name, description))
        connection.commit()
        cursor.close()
        connection.close()
        flash("Data Inserted Successfully")
    return redirect(url_for('Home'))

@app.route('/form')
def form():
    return render_template('form.html')  # Render the form

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Use request.args for GET
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movie_details WHERE name LIKE %s", ('%' + query + '%',))
    search_results = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('search_results.html', data=search_results, query=query)
#query = http://127.0.0.1/search?query=frozen
@app.route('/remove')
def remove():
    return render_template('delete.html')  # Render the delete page

@app.route('/delete', methods=["POST"])
def delete():
    if request.method=="POST":
        name = request.form['name']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("delete FROM movie_details WHERE name LIKE %s", ('%' + name + '%',))
        connection.commit()
        cursor.close()
        connection.close()
    return redirect(url_for('Home'))  

app.run(host="0.0.0.0", port=80, debug=True)

