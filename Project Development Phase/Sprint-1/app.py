from flask import Flask, render_template, request,session,redirect,url_for,g,flash
import ibm_db
from flask_mail import Mail, Message
from random import randint

connectionstring="DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;PROTOCOL=TCPIP;UID=tgv79601;PWD=hedIlL8ICZwxQhwP;SECURITY=SSL;"
connection = ibm_db.connect(connectionstring, '', '')

print(ibm_db.active(connection))

global account

class user:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password

app = Flask(__name__)
app.secret_key="123456789"
mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = '2k19cse060@kiot.ac.in'
app.config['MAIL_PASSWORD'] = 'uxcvcgxchojpwtfd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
@app.route('/home')
def home():
    try:
        return render_template('Home.html')
    except:
        return render_template('autent/Login.html')

@app.route('/signin')
def signin():
    return render_template("autent/Login.html")

@app.route("/adduser", methods=['POST'])
def adduser():
    if request.method == 'POST':
        name = request.form.get('name')
        """gender = request.form.get('gender')"""
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        
        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            flash("You are already a member...!!!",'danger')
            return render_template('autent/Signup.html', msg="Please login using your details")
        else:
            otp = randint(000000, 999999)
            vemail = email
            msg = Message(subject='OTP', sender='hackjacks@gmail.com',recipients=[vemail])
            msg.body = "You have succesfully registered on Nutritional Assist!\n\nUse the OTP given below to verify your email ID.\n\t\n\t" + str(otp)
            mail.send(msg)
            
            """insert_sql = "INSERT INTO User VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(connection, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, gender)
            ibm_db.bind_param(prep_stmt, 4, email)
            ibm_db.bind_param(prep_stmt, 5, password)
            ibm_db.execute(prep_stmt)
            return redirect('/signin')"""

@app.route("/checkuser", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        global account
        account = ibm_db.fetch_assoc(stmt)
        if account:
            if (email == str(account['EMAIL']).strip() and password == str(account['PASSWORD']).strip()):
                session['id'] = account['PHONE']
                g.record=1
                return redirect(url_for('home'))
            else:
                g.record=0
            if g.record!=1:
                flash("Username or Password Mismatch...!!!",'danger')
                return render_template('autent/Login.html', msg="Email is invalid")
        else:
            flash("Account doesn't exist...!!!",'danger')
            return render_template('autent/Login.html', msg="Enter detail again or signup for new account")
    else:
        return render_template('autent/Login.html',msg="Retry")
    
@app.before_request
def before_request():
    global account
    if 'id' in session:
        sql = "SELECT * FROM user WHERE phone =?"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.bind_param(stmt, 1, session['id'])
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        if account:
            g.user = account

@app.route('/user')
@app.route('/check')
def user():
    if not g.user:
        return render_template('autent/Login.html')
    return render_template('autent/Check.html')
        
@app.route('/signup')
def signup():
    return render_template("autent/Signup.html")

@app.route('/profile')
def profile():
    return render_template("Profile.html")

@app.route('/dashboard')
def dashboard():
    return render_template("Dashboard.html")

@app.route('/validation')
def validation():
    return render_template("autent/Validation.html")

@app.route('/signout')
def signout():
    session.clear()
    g.record=0
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template("About.html")

if __name__ == '__main__':
    app.run(debug=True)