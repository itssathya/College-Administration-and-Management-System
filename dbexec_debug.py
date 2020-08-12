import ast
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="sathya",
  passwd="password",
  database="camsdb"
)
mycursor = mydb.cursor()




mycursor.execute("TRUNCATE TABLE classtt")

myresult=mycursor.fetchall()
print(myresult)
myresult=myresult[0][0]

myresult = ast.literal_eval(myresult)

print()
print()

print(myresult[0])
