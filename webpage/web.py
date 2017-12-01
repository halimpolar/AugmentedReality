from flask import Flask, render_template, json, request,redirect,session
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os
import uuid

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'AugmentedDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.config['UPLOAD_FOLDER'] = 'static/Uploads'

@app.route('/')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _SID= request.form['inputSID']
        _role = request.form['inputRole']
        _marker = request.form['inputAruco']

        # validate the received values
        if _SID and _name and _role and _marker:
            
            # All Good, let's call MySQL
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser',(_SID,_name,_role,_marker))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # file upload handler code will be here
    if request.method == 'POST':
        _username = request.form['inputName']
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return json.dumps({'filename': file.filename})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(port=5000)