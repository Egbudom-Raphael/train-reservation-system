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
    conn.close()
    return validate


def register_customer(data):
    # cost=list(data)
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customer_info(username, lastname, middlename, firstname, email, phonenumber, password) VALUES(?,?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()

