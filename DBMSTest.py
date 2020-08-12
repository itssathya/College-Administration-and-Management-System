import mysql.connector
import ast
def userDataRet():
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT uname, fname, dept FROM facdatalog")

    myresult = mycursor.fetchall()

    return myresult


def dataRetrieve(user,pwd):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM usrdata")

    myresult = mycursor.fetchall()
    for i in myresult:
        if i[0]==user:
            if i[1]==pwd:
                return [True,i[0],i[2]]
            return ["Passfail"]
    return [False]

#___________________________________________________________________-


def facReg(uname,pwd,fname,dept,email):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    ttdef=[]
    for i in range(6):
        templ=[]
        for j in range (8):
            templ.append('')
        ttdef.append(templ)
    mycursor = mydb.cursor()
    sql = "INSERT INTO facdatalog (uname, pwd, fname, dept, email, tt, attd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (uname,pwd,fname,dept,email,str(ttdef),"")
    mycursor.execute(sql, val)
    sql = "INSERT INTO usrdata (uname, pwd, role) VALUES (%s, %s, %s)"
    val = (uname,pwd,"Faculty")
    mycursor.execute(sql, val)
    sql = "INSERT INTO facdatafull (uname, tt, attd) VALUES (%s, %s, %s)"
    val = (uname,"","")
    mycursor.execute(sql, val)
    mydb.commit()

def timeSet(tt,uname):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE facdatalog SET tt = %s WHERE uname = %s"
    val = (str(tt),str(uname))
    mycursor.execute(sql,val)
    mydb.commit()

def stuReg(uname,pwd,fname,dept,sec):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO studdatalog (uname, pwd, fname, dept, sec) VALUES (%s, %s, %s, %s, %s)"
    val = (uname,pwd,fname,dept,sec)
    mycursor.execute(sql, val)
    sql = "INSERT INTO usrdata (uname, pwd, role) VALUES (%s, %s, %s)"
    val = (uname,pwd,"Student")
    mycursor.execute(sql, val)
    sql = "INSERT INTO studdatafull (uname, tt, att) VALUES (%s, %s, %s)"
    val = (uname,"","")
    mycursor.execute(sql, val)
    mydb.commit()

def onDutyPOST(datalist,uname):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM studdatalog WHERE uname = %s"
    adr = (uname, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    sql = "INSERT INTO onduty (id, name, dept, sec, ename, einst, edate, attd, reason) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (myresult[0][0], myresult[0][2], myresult[0][3], myresult[0][4], datalist[2], datalist[0], datalist[1], "", datalist[3])
    mycursor.execute(sql,val)
    mydb.commit()

def ODRetrieve():
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM onduty")
    myresult = mycursor.fetchall()
    return myresult

def ODAction(nlist):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("TRUNCATE TABLE onduty")
    mydb.commit()
    for val in nlist:
        sql="INSERT INTO onduty (id, name, dept, sec, ename, einst, edate, attd, reason) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql,val)
    mydb.commit()

def classAdd(dept,sec):
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    ttdef=[]
    for i in range(6):
        templ=[]
        for j in range (8):
            templ.append('')
        ttdef.append(templ)            
    mycursor = mydb.cursor()
    sql = "INSERT INTO classtt (class,tt,dept) VALUES (%s, %s, %s)"
    classis=dept+" "+sec
    val = (classis,str(ttdef),dept)
    mycursor.execute(sql,val)
    mydb.commit()

def classRet():
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT class FROM classTT")

    myresult = mycursor.fetchall()

    return myresult

def TTRet():
    mydb = mysql.connector.connect(
      host="localhost",
      user="sathya",
      passwd="password",
      database="camsdb"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT tt FROM facdatalog")

    myresult = mycursor.fetchall()
    myresult=myresult[0][0]

    myresult = ast.literal_eval(myresult)

    return myresult
    
#------------------------------------------------------------------
    
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="sathya",
  passwd="password",
  database="camsdb"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE customers")"""

    
