
from flask import Flask, render_template, request
import ibm_db

connectionstring="DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;PROTOCOL=TCPIP;UID=sdd68044;PWD=RVCMJUDrmS2iL2xl;SECURITY=SSL;"
connection = ibm_db.connect(connectionstring, '', '')

print(ibm_db.active(connection))

username = None

app = Flask(__name__)

@app.route('/')
def root():
    if(username!=None):return render_template("Home.html", username = username);
    else:return render_template("Home.html", username = "Guest");

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
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')

        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        return render_template('autent/Signup.html', msg="You are already a member, please login using your details")
    else:
        insert_sql = "INSERT INTO User VALUES (?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(connection, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, username)
        ibm_db.bind_param(prep_stmt, 3, phone)
        ibm_db.bind_param(prep_stmt, 4, email)
        ibm_db.bind_param(prep_stmt, 5, password)
        ibm_db.execute(prep_stmt)
    return render_template('autent/Login.html')

@app.route("/checkuser", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        global username
        username = ibm_db.result(stmt,'USERNAME')

        if account:
            if (password == str(account['PASSWORD']).strip()):
                return render_template('Home.html',username = username)
            else:
                return render_template('autent/Login.html', msg="Password is invalid")
        else:
            return render_template('autent/Login.html', msg="Email is invalid")
    else:
        return render_template('autent/Login.html')
    
@app.route('/signout')
def signout():
    global username
    username = None
    return render_template("Home.html", username = "Guest");


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    username = username
