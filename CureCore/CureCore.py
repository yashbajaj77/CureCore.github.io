from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Henupriti144@",
    database="patients_database"
)

# Define a function to fetch patient data from MySQL
def fetch_patient_data():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients")
    patients_data = cursor.fetchall()
    cursor.close()
    return patients_data

# Define the route to render the home page
@app.route('/')
def home():
    # Fetch patient data
    patients_data = fetch_patient_data()
    return render_template('index.html', patients_data=patients_data)

if __name__ == '__main__':
    app.run(debug=True)