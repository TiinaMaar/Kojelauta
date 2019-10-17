from flask import Flask
import mysql.connector as mariadb
app = Flask(__name__)
@app.route("/")
def hello():
    mariadb_connection = mariadb.connect(host='172.17.0.3', port='3306',user='tballs', password='big', database='tballs')
    ##mariadb_connection = mariadb.connect(user='python_user', password='some_pass', database='employees')
    cursor = mariadb_connection.cursor()
    try:
        cursor.execute("SELECT O_ryhmaID, nimi FROM O_ryhma WHERE O_ryhmaID=1")
        # where mukana:  "SELECT first_name,last_name FROM employees WHERE first_name=%s"
    except mariadb.Error as error:
        return("Virhe {}".format(error))
    for O_ryhmaID, nimi in cursor:
        rivi = ("Ryhmä: {}, Ryhmän nimi: {}").format(str(O_ryhmaID),nimi)
    mariadb_connection.close()
    return (rivi)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

