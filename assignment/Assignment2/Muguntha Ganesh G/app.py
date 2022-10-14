
from flask import Flask, render_template, request
import ibm_db

connectionstring="DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;PROTOCOL=TCPIP;UID=sdd68044;PWD=RVCMJUDrmS2iL2xl;SECURITY=SSL;"
connection = ibm_db.connect(connectionstring, '', '')

print(ibm_db.active(connection))

username = None

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("Home.html", username = username);

@app.route('/check')
def check():
    if(username == None): return render_template("autent/Signup.html");
    else: return render_template("autent/check.html");

@app.route('/signin')
def signin():
    return render_template("autent/Login.html");

@app.route('/signup')
def signup():
    return render_template("autent/Signup.html");

@app.route('/about')
def about():
    return render_template("About.html");

@app.route("/adduser", methods=['POST'])
def adduser():
    if request.method == 'POST':
        name = request.form.get('name-9315')
        username = request.form.get('username-a30d')
        email = request.form.get('email-2ea9')
        password = request.form.get('password-a30d')
        phone = request.form.get('phone-fe4c')

        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        return render_template('signup.html', msg="You are already a member, please login using your details")
    else:
        insert_sql = "INSERT INTO User VALUES (?,?,?,?)"
        prep_stmt = ibm_db.prepare(connection, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, first_name)
        ibm_db.bind_param(prep_stmt, 2, last_name)
        ibm_db.bind_param(prep_stmt, 3, email)
        ibm_db.bind_param(prep_stmt, 4, password)
        ibm_db.execute(prep_stmt)
    return render_template('signin.html')

app.run(debug=True);
