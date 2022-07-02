import secrets
import sqlite3
import re
import datetime
import string
import smtplib
import credentials as cd
import urllib.request
from collections import namedtuple
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.pyplot as plt

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
    conn = sqlite3.connect("trainplus.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE username=?", [(name)])
    username = cursor.fetchall()
    conn.close()
    if username:
        return True
    else:
        return False

def check_email_exists(email):
    conn = sqlite3.connect("trainplus.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE email=?", [(email)])
    mail = cursor.fetchall()
    conn.close()
    if mail:
        return True
    return False

def check_phone_exists(phone):
    conn = sqlite3.connect("trainplus.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_info WHERE phonenumber=?", [(phone)])
    num = cursor.fetchall()
    conn.close()
    if num:
        return True
    else:
        return False

def login_validate(username,password):
    conn = sqlite3.connect("trainplus.db")
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
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customer_info(username, lastname, middlename, firstname,gender, email, phonenumber, password,type) VALUES(?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()


#++++++++++++++++++++++++++++++++++++++++++++++booking functions++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_sources():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    sources=set(c.execute("SELECT dep_location FROM schedule ORDER BY dep_location DESC").fetchall())
    conn.commit()
    conn.close()
    source_list=[]
    for i in sources:
        source_list.append(i[0])
    return source_list



def get_destinations(source):
    conn = sqlite3.connect('trainplus.db')
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
    conn = sqlite3.connect('trainplus.db')
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
    conn = sqlite3.connect('trainplus.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    time = c.execute("SELECT time FROM schedule WHERE dep_location=? and arr_location=? and start_date<=? and end_date>=?",(source, dest, date, date)).fetchall()
    conn.commit()
    conn.close()
    return time

def get_schedule_id(source,dest,date,time):
    conn = sqlite3.connect('trainplus.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    schedule = c.execute("SELECT schedule_id FROM schedule WHERE dep_location=? and arr_location=? and start_date<=? and end_date>=? and time=?",(source, dest, date, date,time,)).fetchall()
    conn.commit()
    conn.close()
    return schedule[0][0]

def get_price(source,dest,time):
    conn = sqlite3.connect('trainplus.db')
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
    conn = sqlite3.connect('trainplus.db')
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
def get_seats(cls='first class',schedule_num='LXM4CBI5'):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    seats=c.execute("SELECT seat_num FROM tickets where schedule_num=? AND class=?",(schedule_num,cls,)).fetchall()
    conn.commit()
    conn.close()
    new_list=[]
    for i in seats:
        new_list.append(int(i[0][3:]))
    return new_list


def register_all(tknum,seatnum,schedule,name,date,time,cls,username):
    conn = sqlite3.connect('trainplus.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                                     sqlite3.PARSE_COLNAMES)
    data=[tknum,seatnum,schedule,name,date,time,cls,username]
    c = conn.cursor()
    c.execute("INSERT INTO tickets VALUES(?,?,?,?,?,?,?,?)",data)
    conn.commit()
    conn.close()

def store_card_details(data,username):
    data.append(username)
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.execute("UPDATE customer_info SET card_num=?, exp_month=?, exp_year=?, card_holder=?, card_code=? WHERE username=?",data)
    conn.commit()
    conn.close()

def forget_card_details(username):
    data=[None,None,None,None,None,username]
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.execute("UPDATE customer_info SET card_num=?, exp_month=?, exp_year=?, card_holder=?, card_code=? WHERE username=?",data)
    conn.commit()
    conn.close()

def get_card_details(username):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    card=c.execute("SELECT card_num, exp_month, exp_year, card_holder, card_code FROM customer_info WHERE username=?",(username,)).fetchone()
    conn.commit()
    conn.close()
    return list(card)

def send_mail(tknum,email):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    data = c.execute("""SELECT ticket_num,seat_num,train_id,p_name,dep_date,dep_time,class,dep_location,arr_location
                        FROM tickets
                        INNER JOIN schedule
                        ON tickets.schedule_num = schedule.schedule_id
                        WHERE ticket_num=?""", (tknum,)).fetchone()
    conn.commit()
    conn.close()
    print(data)
    message=f"""Subject: noreply\n
            Your ticket\n
            Ticket number: \t{data[0]}\n
            Seat number: \t{data[1]}\n
            Train number: \t{data[2]}\n
            Passenger name: \t{data[3].title()}\n
            Departure date: \t{data[4]}\n
            Departure time: \t{data[5]}\n
            Seat class: \t{data[6]}\n
            Departure station: \t{data[7]}\n
            Arrival station: \t{data[8]}\n
            """
    try:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(cd.sender, cd.password)
        s.sendmail(cd.sender,email,message)
        s.quit()
    except:
        pass

def check_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def get_full_booking(username='sugarpops'):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    data=c.execute("""SELECT ticket_num,seat_num,train_id,p_name,dep_date,dep_time,class,dep_location,arr_location
                        FROM tickets
                        INNER JOIN schedule
                        ON tickets.schedule_num = schedule.schedule_id
                        WHERE username=?
                        ORDER BY dep_date""",(username,)).fetchall()
    conn.commit()
    conn.close()
    return data

def update_customer_data(data):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.executemany("""UPDATE customer_info
                        SET lastname=?, middlename=?, firstname=?, gender=?, email=?, phonenumber=?, password=?
                        WHERE username=?""", data)
    conn.commit()
    conn.close()

# +++++++++++++++++++++++++++++++++++++++++++++++++admin functions+++++++++++++++++++++++++++++++++++++++++++++++
def get_all_trains():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    trains=c.execute("SELECT * FROM trains").fetchall()
    conn.commit()
    conn.close()
    return trains

def disable_train(trainid):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.execute("UPDATE trains SET status='out of service' WHERE train_id=?",(trainid,))
    conn.commit()
    conn.close()

def generate_train_id():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    num=c.execute("SELECT COUNT(*) FROM trains").fetchone()
    conn.commit()
    conn.close()
    num=num[0]+1
    if num<10:
        x = ''.join('TIR-1'+'00' +f'{num}')
    elif num<100:
        x = ''.join('TIR-1'+'0' +f'{num}')
    elif num<1000:
        x = ''.join('TIR-1'+'' +f'{num}')
    else:
        x = ''.join('TIR-'+f'{1000+num}')

    return x

def add_new_train(name,fc,bc,rc):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.execute("INSERT INTO trains VALUES(?,?,?,?,?,?)",(generate_train_id(),name,fc,bc,rc,'active',))
    conn.commit()
    conn.close()

def validate_train(name):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    x=c.execute("SELECT * FROM trains WHERE name=?",(name,)).fetchone()
    conn.commit()
    conn.close()
    return x


def edit_train(trainid,name,fc,bc,rc,status):
    data=[name,fc,bc,rc,status,trainid]
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    c.execute("UPDATE trains SET name=?, first_class_capacity=?, business_class_capacity=?, regular_coach_capacity=?, status=? WHERE train_id=?",data,)
    conn.commit()
    conn.close()

def get_all_schedules():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    trains=c.execute("SELECT * FROM schedule").fetchall()
    conn.commit()
    conn.close()
    return trains

def get_train_list():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    trains=c.execute("SELECT name FROM trains ").fetchall()
    conn.commit()
    conn.close()
    lst=[]
    for i in trains:
        lst.append(i[0])
    return lst
def get_all_destinations():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    dest = set(c.execute("SELECT arr_location FROM schedule").fetchall())
    conn.commit()
    conn.close()
    dest_list=[]
    for i in dest:
        dest_list.append(i[0])
    return dest_list

def register_schedule(data):
    conn = sqlite3.connect('trainplus.db', detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("INSERT INTO schedule VALUES(?,?,?,?,?,?,?,?,?,?)", data,)
    conn.commit()
    conn.close()

def get_intersect(s1,e1,s2,e2):
    Range=namedtuple('Range',['start','end'])
    r1=Range(start=s1,end=e1)
    r2=Range(start=s2,end=e2)
    latest_start=max(r1.start,r2.start)
    earliest_end=min(r1.end,r2.end)
    delta=(earliest_end-latest_start).days+1
    overlap=max(0,delta)
    return overlap

def validate_schedule(source,dest,time,start,end):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    dates=c.execute("SELECT start_date,end_date,schedule_id FROM schedule WHERE dep_location=? AND arr_location=? AND time=?", (source,dest,time),).fetchall()
    conn.commit()
    conn.close()
    x=0
    if dates:
        for data in dates:
            s2=datetime.datetime.strptime(data[0],"%Y-%m-%d").date()
            e2=datetime.datetime.strptime(data[1],"%Y-%m-%d").date()
            x+=get_intersect(start,end,s2,e2)
            if x>0:
                break
        if x==0:
            return False
        else:
            return data[2]
    else:
        return False

def get_trainid(name):
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    data=c.execute("SELECT train_id FROM trains WHERE name=?", (name,)).fetchone()
    conn.commit()
    conn.close()
    return data[0]

def get_all_tickets():
    conn = sqlite3.connect('trainplus.db')
    c = conn.cursor()
    data=c.execute("""SELECT username,ticket_num,seat_num,train_id,p_name,dep_date,dep_time,class,dep_location,arr_location
                        FROM tickets
                        INNER JOIN schedule
                        ON tickets.schedule_num = schedule.schedule_id
                        ORDER BY dep_date""").fetchall()
    conn.commit()
    conn.close()
    return data

def plot_pie():
    sources=get_sources()
    tickets=get_all_tickets()
    location=[]
    count=0
    sus2=[]
    for x in sources:
        sus2.append(x[:-8])
        for y in tickets:
            if x in y[8]:
                count+=1
        location.append(count)
        count=0
    lightgrey='#F1F1F1'
    greencolor = '#00f18c'

    piechart = Figure(figsize=(3, 3), dpi=70, facecolor=lightgrey)
    bx = piechart.add_subplot(111)
    # exploded = [0.1, 0.2, 0.1, 0,0]
    patches, texts, autotexts = bx.pie(location, autopct='%1.1f%%')
    bx.set_title('BOARDING RATES', color='r',fontsize=14, font='Arial')
    for text in texts:
        text.set_color(greencolor)

    for autotext in autotexts:
        autotext.set_color('white')
    bx.axis('equal')
    piechart.legend(labels=sus2, loc='lower center', ncol=1)
    return piechart

def plot_pie2():
    dest=get_all_destinations()
    tickets=get_all_tickets()
    location=[]
    count=0
    for x in dest:
        for y in tickets:
            if x in y[9]:
                count+=1
        location.append(count)
        count=0
    lightgrey='#F1F1F1'
    greencolor = '#00f18c'

    piechart = Figure(figsize=(3, 3), dpi=75, facecolor=lightgrey)
    bx = piechart.add_subplot(111)
    # exploded = [0.1, 0, 0, 0]
    patches, texts, autotexts = bx.pie(location, autopct='%1.1f%%')
    bx.set_title('DESTINATION RATES', color='#110445',fontsize=14, font='Arial')
    for text in texts:
        text.set_color(greencolor)

    for autotext in autotexts:
        autotext.set_color('white')
    bx.axis('equal')
    piechart.legend(labels=dest,loc='lower center',ncol=1)
    return piechart


def plot_barchart():
    sources = get_sources()
    tickets = get_all_tickets()
    location = []
    count = 0
    sus2 = []
    for x in sources:
        sus2.append(x[:-8])
        for y in tickets:
            if x in y[8]:
                count += 1
        location.append(count)
        count = 0
    lightgrey='#F1F1F1'
    greencolor = '#00f18c'
    figure = Figure(figsize=(5, 2.2), dpi=85, facecolor=lightgrey)
    ax = figure.add_subplot(111)
    ax.set_facecolor(lightgrey)
    x_axis = np.arange(len(location))
    j=1
    for i in sus2:
        ax.bar(x_axis + 0.15*j, location[j-1], width=0.15, label=i)
        # print(i)
        j+=1
    ax.set_xticks(0.35 + x_axis)
    ax.set_xticklabels(sources)
    # plt.xticks(0.35+x_axis, states)
    ax.set_xlabel('stations', color=greencolor)
    ax.set_ylabel('total tickets booked'.upper(), color='r')
    ax.set_title('BOOKING RATES', color='#110445', font='Arial')
    ax.set_facecolor(lightgrey)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color(lightgrey)
    ax.spines['right'].set_color(lightgrey)
    ax.tick_params(axis='x', colors=lightgrey)
    ax.tick_params(axis='y', colors='#110445')
    ax.grid(True, color='white', linestyle=':')
    ax.legend(loc='lower right')
    return figure




