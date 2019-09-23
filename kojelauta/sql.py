# -*- coding: latin-1 -*-
#!/usr/bin/python
#
""" nämä tarpeen virtuaalikoneessa. python 2 tässä ihan vaan
sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y docker.io
sudo docker build -t mariadb .
sudo docker run -d --name mariadb mariadb
sudo apt-get install -y python
sudo apt install -y python-pip
sudo apt-get install -y nano
pip install mysql-connector
git clone https://github.com/TiinaMaar/Kojelauta.git
cd Kojelauta
git checkout sql
cd kojelauta
python sql.py//
"""

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='172.17.0.2', port='3306',user='tballs', password='big', database='tballs')
##mariadb_connection = mariadb.connect(user='python_user', password='some_pass', database='employees')
cursor = mariadb_connection.cursor()

try:
    cursor.execute("SELECT O_ryhmaID, nimi FROM O_ryhma")
# where mukana:  "SELECT first_name,last_name FROM employees WHERE first_name=%s"
except mariadb.Error as error:
  print("Virhe {}".format(error))

for O_ryhmaID, nimi in cursor:
    print("Ryhmä: {}, Ryhmän nimi: {}").format(str(O_ryhmaID),nimi)
#"first_name, last_name in cursor"

#lisäys
mariadb_connection.close()
