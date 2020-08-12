import DBMSTest as dbt
import notifOD as notif
from StructClasses import Queue
from flask import Flask, render_template,request,redirect,url_for,flash
from flask_bootstrap import Bootstrap
mon=[]
tue=[]
wed=[]
thur=[]
fri=[]
sat=[]
fintt=[]
user=None
pwd=None
usrsess=None
app = Flask(__name__)
app.secret_key = 'some_secret'
def TTSMod():
   global mon,tue,wed,thur,fri,sat,fintt
   mon=['Monday']
   tue=['Tuesday']
   wed=['Wednesday']
   thur=['Thursday']
   fri=['Friday']
   sat=['Saturday']
   fintt=[]
   return
Bootstrap(app)
@app.route('/')
def student():
   return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
   global user,pwd
   if request.method == 'POST':
      user=request.form['user']
      pwd=request.form['pass']
      return redirect(url_for('index'))

@app.route('/index')
def index():
   global user,pwd,usrsess
   temp=dbt.dataRetrieve(user,pwd)
   if temp[0]==True:
      usrsess=temp[1]
      if temp[2]=="Faculty":
         return render_template('facConsole.html',name=usrsess)
      elif temp[2]=="Student":
         return render_template('studConsole.html',name=usrsess)
      elif temp[2]=="Superuser":
         return render_template('suconsole.html',name=usrsess)
   elif temp[0]=="Passfail":
      return redirect(url_for('student'))
   else:
      return redirect(url_for('student'))

@app.route('/facData',methods=['GET','POST'])
def facData():
   temp=dbt.userDataRet()
   return render_template('facData.html',users=temp)

@app.route('/TTDisp',methods=['GET','POST'])
def TTDisp():
   temp1=dbt.TTRet()
   return render_template('TTDisp.html',tt=temp1)

@app.route('/facReg',methods=['GET','POST'])
def facReg():
   if request.method == 'GET':
      return render_template('facReg.html',ntf="")
   elif request.method == 'POST':
      uname=request.form['usernme']
      pwd=request.form['pwd']
      fname=request.form['fname']
      dept=request.form['dept']
      email=request.form['emailid']
      dbt.facReg(uname,pwd,fname,dept,email)
      return render_template('facReg.html',ntf="Faculty Admission Successful!")
      
@app.route('/setTT',methods=['GET','POST'])
def setTT():
   if request.method == 'GET':
      classes1=dbt.classRet()
      return render_template('setTT.html',sett="",classes=classes1)
   elif request.method == 'POST':
      TTSMod()
      for i in range (1,9):
         tc=request.form['m'+str(i)]
         mon.append(tc)
      for i in range (1,9):
         tc=request.form['tu'+str(i)]
         tue.append(tc)
      for i in range (1,9):
         tc=request.form['w'+str(i)]
         wed.append(tc)
      for i in range (1,9):
         tc=request.form['th'+str(i)]
         thur.append(tc)
      for i in range (1,9):
         tc=request.form['f'+str(i)]
         fri.append(tc)
      for i in range (1,9):
         tc=request.form['s'+str(i)]
         sat.append(tc)
      fintt.append(mon)
      fintt.append(tue)
      fintt.append(wed)
      fintt.append(thur)
      fintt.append(fri)
      fintt.append(sat)
      dbt.timeSet(fintt,usrsess)
      return render_template('setTT.html',sett="Timetable Successfully Set.")
@app.route('/studOD',methods=['GET','POST'])
def studOD():
   global user,pwd
   if request.method == 'GET':
      return render_template('onDuty.html',ntf="")
   elif request.method == 'POST':
      datalist=[]
      datalist.append(request.form['einst'])
      datalist.append(request.form['edate'])
      datalist.append(request.form['ename'])
      datalist.append(request.form['reason'])
      dbt.onDutyPOST(datalist,usrsess)
      return render_template('onDuty.html',ntf="On Duty Submitted. You will be notified of progress by E-Mail.")

@app.route('/HoDOD',methods=['GET','POST'])
def HoDOD():
   if request.method == 'GET':
      global q
      ab=dbt.ODRetrieve()
      q=None
      q=Queue()
      for i in ab:
         q.enqueue(i)
      return render_template('onDutyHoD.html',users=q.list)
   elif request.method == 'POST':
      ans=request.form['ans']
      if ans == "Approve":
         dat1=q.dequeue()
         dbt.ODAction(q.list)
         notif.ODApproveSMTP(dat1)
      elif ans == "Reject":
         q.dequeue()
         dbt.ODAction(q.list)
         

@app.route('/stuReg',methods=['GET','POST'])
def stuReg():
   if request.method == 'GET':
      return render_template('stuReg.html',ntf="")
   elif request.method == 'POST':
      uname=request.form['usernme']
      pwd=request.form['pwd']
      fname=request.form['fname']
      dept=request.form['dept']
      sec=request.form['sec']
      dbt.stuReg(uname,pwd,fname,dept,sec)
      return render_template('stuReg.html',ntf="Student Account Created")

@app.route('/addClass',methods=['GET','POST'])
def addClass():
   if request.method == 'GET':
      return render_template('addClass.html')
   elif request.method == 'POST':
      dept=request.form['dept']
      sec=request.form['sec']
      dbt.classAdd(dept,sec)

@app.route('/logout',methods=['GET','POST'])
def logout():
   user=None
   pwd=None
   usrsess=None
   return redirect(url_for('student'))
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == '__main__':
   app.run(debug=True)
