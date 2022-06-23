import secrets
import sqlite3
import re
import datetime
import string
import smtplib
import credentials as cd
import urllib.request

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
    date=datetime.datetime.today().date()
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    sources=set(c.execute("SELECT dep_location FROM schedule WHERE end_date>=?",(date,)).fetchall())
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

def convert_to_datetime(date='2022-09-5'):
    return datetime.datetime.strptime(date,"%Y-%m-%d").date()

def get_time(source,dest,date):
    datedata=convert_to_datetime(date)
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    time = set(c.execute("SELECT time,start_date,end_date FROM schedule WHERE dep_location=? and arr_location=?",(source,dest,)).fetchall())
    conn.commit()
    conn.close()
    time_list=[]
    time=list(time)
    for i in range(len(time)):
        if datedata>=convert_to_datetime(time[i][1]) and datedata<=convert_to_datetime(time[i][2]):
            time_list.append(time[i][0])
    return time_list

def get2_time():
    source='Mobolaji Johnson Station'
    dest='Obafemi Awolowo Station'
    date=convert_to_datetime('2022-07-10')
    conn = sqlite3.connect('railly.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    time = c.execute("SELECT time FROM schedule WHERE dep_location=? and arr_location=? and start_date<=? and end_date>=?",(source, dest, date, date)).fetchall()
    conn.commit()
    conn.close()
    return time

def get_schedule_id(source,dest,date,time):
    conn = sqlite3.connect('railly.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    schedule = c.execute("SELECT schedule_id FROM schedule WHERE dep_location=? and arr_location=? and start_date<=? and end_date>=? and time=?",(source, dest, date, date,time,)).fetchall()
    conn.commit()
    conn.close()
    return schedule[0][0]

def get_price(source,dest,time):
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    time = c.execute("SELECT first_class_price, business_class_price, regular_coach_price FROM schedule WHERE dep_location=? and arr_location=? and time=?",(source, dest, time,)).fetchone()
    conn.commit()
    conn.close()
    return list(time)

def generate_ticket_num():
    x=''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return x

def generate_schedule_num():
    x=''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    return x

def get_num_of_seats(schedule_id,cls):
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    trainid = c.execute("SELECT train_id FROM schedule WHERE schedule_id=?",(schedule_id,)).fetchone()
    trainid=trainid[0]
    if cls=='first class':
        num=c.execute("SELECT first_class_capacity FROM trains WHERE train_id=?",(trainid,)).fetchone()
    elif cls=='business class':
        num=c.execute("SELECT business_class_capacity FROM trains WHERE train_id=?",(trainid,)).fetchone()
    elif cls=='regular coach':
        num=c.execute("SELECT regular_coach_capacity FROM trains WHERE train_id=?",(trainid,)).fetchone()
    conn.commit()
    conn.close()
    num=num[0]
    return num
# print(get_num_of_seats('WUJ4QQKI','business class'))
def get_seats(cls='first class',schedule_id='LXM4CBI5'):
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    seats=c.execute("SELECT seat_num FROM tickets where schedule_id=? AND class=?",(schedule_id,cls,)).fetchall()
    conn.commit()
    conn.close()
    new_list=[]
    for i in seats:
        new_list.append(int(i[0][3:]))
    return new_list


def register_all(tknum,seatnum,schedule,name,date,time,cls,username):
    conn = sqlite3.connect('railly.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                                     sqlite3.PARSE_COLNAMES)
    data=[tknum,seatnum,schedule,name,date,time,cls,username]
    c = conn.cursor()
    c.execute("INSERT INTO tickets VALUES(?,?,?,?,?,?,?,?)",data)
    conn.commit()
    conn.close()

def store_card_details(data,username):
    data.append(username)
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    c.execute("UPDATE customer_info SET card_num=?, exp_month=?, exp_year=?, card_holder=?, card_code=? WHERE username=?",data)
    conn.commit()
    conn.close()

def forget_card_details(username):
    data=[None,None,None,None,None,username]
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    c.execute("UPDATE customer_info SET card_num=?, exp_month=?, exp_year=?, card_holder=?, card_code=? WHERE username=?",data)
    conn.commit()
    conn.close()

def get_card_details(username):
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()
    card=c.execute("SELECT card_num, exp_month, exp_year, card_holder, card_code FROM customer_info WHERE username=?",(username,)).fetchone()
    conn.commit()
    conn.close()
    return list(card)

def send_mail(tknum,seatnum,train_name,name,date,time,cls,email):
    message=f"""Subject: YOUR TICKET\n
            Ticket number: \t{tknum}\n
            Seat number: \t{seatnum}\n
            Travel number: \t{train_name}\n
            Passenger name: \t{name.title()}\n
            Departure date: \t{date}\n
            Departure time: \t{time}\n
            Seat class: \t{cls}\n
            """
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(cd.sender, cd.password)
    s.sendmail(cd.sender,email,message)
    s.quit()

def check_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
