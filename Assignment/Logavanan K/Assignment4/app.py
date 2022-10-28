
from flask import Flask, render_template, request
import ibm_db

connectionstring="DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;PROTOCOL=TCPIP;UID=tls73368;PWD=eM9OA97V5rLiquSp;SECURITY=SSL;"
connection = ibm_db.connect(connectionstring, '', '')

print(ibm_db.active(connection))


app = Flask(__name__)

@app.route('/')
def root():
    return render_template("Home.html");

# '''@app.route('/check')
# def check():
#     if(username == None): return render_template("autent/signup.html");
#     else: return render_template("check.html");'''

@app.route('/login')
def signin():
    return render_template("login.html");

@app.route('/signup')
def signup():
    return render_template("signup.html");

@app.route('/about')
def about():
    return render_template("About.html");

@app.route("/adduser", methods=['POST'])
def adduser():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        #username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')        

        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        return render_template('signup.html', msg="You are already a member, please login using your details")
    else:
        insert_sql = "INSERT INTO user VALUES (?,?,?,?)"
        prep_stmt = ibm_db.prepare(connection, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        #ibm_db.bind_param(prep_stmt, 2, username)
        ibm_db.bind_param(prep_stmt, 2, phone)
        ibm_db.bind_param(prep_stmt, 3, email)
        ibm_db.bind_param(prep_stmt, 4, password)
        ibm_db.execute(prep_stmt)
    return render_template('login.html')

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
        #username = ibm_db.result(stmt,'USERNAME')

        if account:
            if (password == str(account['PASSWORD']).strip()):
                return render_template('Home.html',username = username)
            else:
                return render_template('login.html', msg="Password is invalid")
        else:
            return render_template('login.html', msg="Email is invalid")
    else:
        return render_template('login.html')


app.run(debug=True);
