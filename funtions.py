import sqlite3
import re


def check_email(mail):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
    if re.fullmatch(regex, mail):
        return True
    return False  # email is invalid

def check_name(name):
    regex = r"[A-Za-z][-a-zA-Z. ']+"
    if re.fullmatch(regex, name) or name == '' or name == '-':
        return True
    return False  # name is invalid

def check_phone(num):
    regex = r"[0-9+]+[\d]{4,15}"
    if re.fullmatch(regex, num):
        return True
    return False  # name is invalid

def check_pass(password):
    if ' ' in password or password=='':
        return False
    else:
        return True

def check_username_exists(name):
    conn = sqlite3.connect("railly.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE username=?", [(name)])
    username = cursor.fetchall()
    conn.close()
    if username:
        return True
    else:
        return False

def check_email_exists(email):
    conn = sqlite3.connect("railly.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE email=?", [(email)])
    mail = cursor.fetchall()
    conn.close()
    if mail:
        return True
    return False

def check_phone_exists(phone):
    conn = sqlite3.connect("railly.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE phonenumber=?", [(phone)])
    num = cursor.fetchall()
    conn.close()
    if num:
        return True
    else:
        return False

def login_validate(username,password):
    conn = sqlite3.connect("railly.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE username=? and password=?", [(username),(password)])
    validate = cursor.fetchall()
    cursor.execute("SELECT * FROM customer_info WHERE email=? and password=?", [(username),(password)])
    validate2=cursor.fetchall()
    conn.close()
    if validate:
        return validate
    elif validate2:
        return validate2
    else:
        return False


def register_customer(data):
    # cost=list(data)
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customer_info(username, lastname, middlename, firstname,gender, email, phonenumber, password,type) VALUES(?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()


#++++++++++++++++++++++++++++++++++++++++++++++booking functions++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_sources():
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    sources=set(c.execute("SELECT dep_location FROM schedule").fetchall())
    conn.commit()
    conn.close()
    source_list=[]
    for i in sources:
        source_list.append(i[0])
    return source_list

def get_destinations(source):
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    dest = set(c.execute("SELECT arr_location FROM schedule WHERE dep_location=?",(source,)).fetchall())
    conn.commit()
    conn.close()
    dest_list=[]
    for i in dest:
        dest_list.append(i[0])
    return dest_list

def get_time(source,dest):
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    time = set(c.execute("SELECT time FROM schedule WHERE dep_location=? and arr_location=?",(source,dest,)).fetchall())
    conn.commit()
    conn.close()
    time_list=[]
    for i in time:
        time_list.append(i[0])
    return time_list





