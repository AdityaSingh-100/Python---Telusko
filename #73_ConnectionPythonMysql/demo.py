# install pip3 mysql-connector-python in cmd

# One correction, if you are watching in 2022 @04:00 you might be getting  "Authentication plugin 'caching_sha2_password' is not supported" error.
# Just uninstall mysql-connector & install mysql-connector-python.

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaSingh-100",port="3306",database = "python")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

# result = mycursor.fetchall()
result = mycursor.fetchone()

for i in result:
    print(i)