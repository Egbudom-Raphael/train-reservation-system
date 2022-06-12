from tkinter import *
import sqlite3
from matplotlib import pyplot as plt
from skimage.io import imread
from PIL import ImageTk, Image
from time import *
from random import randint

# image connection

img1_path = "C:/Users/Aishwarya Patil/Desktop/FOLDER/PROGRAMS/PYTHON/train1.jpg"
img1 = imread(img1_path)
plt.imshow(img1)
plt.show()

# database connection

con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
'''
con.execute('create table passenger(name varchar not null,mail varchar not null,psw varchar not null,adhar varchar not null,mobile int not null,gender varchar not null,dob varchar not null,age int not null);')

con.execute('create table train(fromcity varchar not null,tocity varchar not null,tno int not null,tname varchar not null,tdate varchar not null,arr_time varchar not null,dep_time varchar not null,amt int not null);')
con.execute("insert into train values(?,?,?,?,?,?,?,?);",('solapur','bangalur',53331,'manglur express','01/07/2020','2:00PM','11:00AM',1000))
con.execute("insert into train values(?,?,?,?,?,?,?,?);",('bangalur','solapur',93945,'golgumbaj','10/07/2020','8:00PM','10:00AM',1000))
con.execute("insert into train values(?,?,?,?,?,?,?,?);",('gadag','tirupati',101102,'super express','10/07/2020','10:00PM','7:30AM',1500))
'''
con.commit()
con.close()


def print_ticket():
    pass


# Raising frames be invoking the frm() with corresponding frame as parameter

def frm(ff):
    if ff == fr:
        # call the reset fun for fr to make a empty entrybox
        l = Label(fr, text='', font=('Arial', 20, 'bold'), fg='brown', bg='white', width=30, height=1)
        l.place(x=700, y=200)
    if ff == fs:
        l = Label(fs, text='', font=('Arial', 20), fg='black', bg='white', width=30)
        l.place(x=800, y=300)
    if ff == fl:
        l = Label(fl, text='', font=('Arial', 20, 'bold'), fg='red', bg='white', width=20)
        l.place(x=600, y=300)
    if ff == flogout:
        l = Label(flogout, text="", bg='white', fg='black', font=('arial', 15, 'bold'), width=30)
        l.place(x=700, y=350)
    if ff == fpsw:
        l = Label(fpsw, text='', font=('Arial', 20, 'bold'), fg='brown', bg='white', width=30, height=3)
        l.place(x=600, y=600)
    if ff == ftbk:
        lab = Label(ftbk, text="", font=('Arial', 15, 'bold'), fg='brown', bg='white', width=40).place(x=300, y=500)
    ff.tkraise()


def pay(ff):
    lab = Label(fend, text='Congratulations!!!\n your seat is reservaed', font=('Arial', 30, 'bold'), fg='brown',
                bg='white').place(x=400, y=300)
    b = Button(fend, text="print ticket", bg='brown', fg='white', activebackground='brown', activeforeground='yellow',
               font=('arial', 30, 'bold'), command=print_ticket).place(x=200, y=600)
    ff.tkraise()


def added_passanger(t_no_bk, name_bk, age_bk, gender, clss_bk):
    tno1 = t_no_bk.get()
    na = name_bk.get()
    ag = age_bk.get()
    cls1 = clss_bk.get()
    gender = gender.get()
    ge = ''
    if gender == 1:
        ge = 'Male'
    else:
        ge = 'Female'
    con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
    res = con.execute('select amt from train where tno=(?);', (tno1,))
    for i in res:
        fa = i[0]
    r = con.execute('select* from passenger;')

    flag = 0
    for i in r:
        # print(i)
        # print(na,i[0],ge,i[5],ag,i[7])
        if na == i[0] and i[7] == int(ag):
            flag = 0
            # print(i[0],i[5],i[7])
            con.execute('insert into tkt_booked values(?,?,?,?,?,?);', (tno1, na, ag, ge, fa, cls1))
            con.commit()
            break
        else:
            # print('pppp')
            flag = 1
    if flag == 1:
        lab = Label(ftbk, text="please register before booking", font=('Arial', 15, 'bold'), fg='brown',
                    bg='white').place(x=300, y=500)
    # con.execute('insert into ticket_booked values(?,?,?,?,?);',(tno1,na,ag,ge,fa))
    # con.commit()
    else:
        lab = Label(ftbk, text="", font=('Arial', 15, 'bold'), fg='brown', bg='white', width=30).place(x=300, y=700)
        lab = Label(ftbk, text=str(1), font=('Arial', 12, 'bold'), fg='black', bg='white', width=10).place(x=100, y=450)
        lab = Label(ftbk, text=cls1, font=('Arial', 12, 'bold'), fg='black', bg='white', width=13).place(x=200, y=450)
        lab = Label(ftbk, text=na, font=('Arial', 12, 'bold'), fg='black', bg='white', width=20).place(x=300, y=450)
        lab = Label(ftbk, text=str(ag), font=('Arial', 12, 'bold'), fg='black', bg='white', width=20).place(x=500,
                                                                                                            y=450)
        lab = Label(ftbk, text=ge, font=('Arial', 12, 'bold'), fg='black', bg='white', width=20).place(x=700, y=450)
        lab = Label(ftbk, text=str(fa), font=('Arial', 12, 'bold'), fg='black', bg='white', width=20).place(x=900,
                                                                                                            y=450)
        # lab=Label(ftbk,text='Action',font=('Arial',12,'bold'),fg='white',bg='brown',width=20).place(x=1100,y=400)
        b = Button(ftbk, text="procced to pay", activebackground="brown", bg="brown", fg="white",
                   font=('Arial', 12, 'bold'), command=lambda: frm(fpay)).place(x=1100, y=450)


def tck_book(ff):
    header = Label(ftbk, text='', font=('Arial', 20, 'bold'), fg='white', bg='brown', width=1500, height=3)
    header.place(x=0, y=0)
    header1 = Label(ftbk, text='Online reservation\nsystem', font=('Arial', 30, 'bold'), fg='white', bg='brown')
    header1.place(x=100, y=0)
    homeb = Button(ftbk, text='Home', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                   height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(f))
    homeb.place(x=700, y=20)
    searchb = Button(ftbk, text='Search', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                     height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(fs))
    searchb.place(x=800, y=20)
    loginb = Button(ftbk, text='Login', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                    height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(fl))
    loginb.place(x=900, y=20)
    regb = Button(ftbk, text='Register', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                  height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(fr))
    regb.place(x=1000, y=20)
    s1, s2 = '_', '_'
    for i in range(100):
        s1 += '_____'
        s2 += '_____'
    lab = Label(ftbk, text=s1, font=('Arial', 10, 'bold'), fg='black', bg='white').place(x=50, y=200)

    lab = Label(ftbk, text='Enter passenger Details', font=('Arial', 30, 'bold'), fg='black', bg='white').place(x=50,
                                                                                                                y=120)
    l = Label(ftbk, text="conform Train No", bg='white', fg='brown', font=('arial', 20, 'bold'))
    l.place(x=600, y=150)
    t_no_bk = Entry(ftbk, width=20, bg='white', fg='black', font=('arial', 15, 'bold'))
    t_no_bk.place(x=850, y=150)
    l = Label(ftbk, text="Class", bg='white', fg='brown', font=('arial', 20, 'bold'))
    l.place(x=1050, y=150)
    clss_bk = StringVar()
    sp = Spinbox(ftbk, width=13, bg='white', fg='black', textvariable=clss_bk,
                 value=('1A', '2A', '3A', 'Sleeper Coatch', 'CC'), font=('arial', -15))
    # sp=Spinbox(ftbk,values=(),textvariable=clss,bg='white'fg='black',width=5)
    sp.place(x=1200, y=150)
    name1 = Label(ftbk, text="Name", bg='white', fg='brown', font=('arial', 20, 'bold'))
    name1.place(x=50, y=250)
    name_bk = Entry(ftbk, width=40, bg='white', fg='black', font=('arial', 15, 'bold'))
    name_bk.place(x=150, y=250)
    age1 = Label(ftbk, text="Age", bg='white', fg='brown', font=('arial', 20, 'bold'))
    age1.place(x=620, y=250)
    age_bk = Entry(ftbk, width=15, bg='white', fg='black', font=('arial', 15, 'bold'))
    age_bk.place(x=680, y=250)

    gdr1 = IntVar()
    gen1 = Label(ftbk, text="Gender", bg='white', fg='brown', font=('arial', 20, 'bold'))
    gen1.place(x=880, y=250)
    gen = Radiobutton(ftbk, variable=gdr1, value=1, text='Male', bg='yellow', fg='brown', font=('arial', 10, 'bold'),
                      width=5).place(x=1000, y=250)
    gen = Radiobutton(ftbk, variable=gdr1, value=2, text='Female', bg='yellow', fg='brown', font=('arial', 10, 'bold'),
                      width=5).place(x=1080, y=250)
    b1 = Button(ftbk, text='Book', bg='brown', fg='white', activebackground='brown', activeforeground='red', width=8,
                font=('Arial', 12, 'bold'), command=lambda: added_passanger(t_no_bk, name_bk, age_bk, gdr1, clss_bk))
    b1.place(x=1200, y=250)
    lab = Label(ftbk, text=s2, font=('Arial', 10, 'bold'), fg='black', bg='white').place(x=50, y=280)

    lab = Label(ftbk, text='Enter passenger Details', font=('Arial', 30, 'bold'), fg='black', bg='white').place(x=50,
                                                                                                                y=300)
    lab = Label(ftbk, text='Note :', font=('Arial', 12), fg='white', bg='black').place(x=550, y=300)
    lab = Label(ftbk, text='( Only single Passenger can be reserved at a time )', font=('Arial', 12), fg='black',
                bg='white').place(x=600, y=302)

    s1 = '_'
    for i in range(100):
        s1 += '_____'
        lab = Label(ftbk, text=s1, font=('Arial', 10, 'bold'), fg='black', bg='white').place(x=50, y=350)
    lab = Label(ftbk, text='Sr.No', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=10).place(x=100, y=400)
    lab = Label(ftbk, text='class', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=10).place(x=200, y=400)
    lab = Label(ftbk, text='Name', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=20).place(x=300, y=400)
    lab = Label(ftbk, text='Age', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=20).place(x=500, y=400)
    lab = Label(ftbk, text='Gender', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=20).place(x=700, y=400)
    lab = Label(ftbk, text='Fare', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=20).place(x=900, y=400)
    lab = Label(ftbk, text='Action', font=('Arial', 12, 'bold'), fg='white', bg='brown', width=20).place(x=1100, y=400)
    frm(ftbk)


# function to display the booking details

def mybooking(ff):
    con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
    m2 = mail_log.get()
    p2 = psw_log.get()
    l1, l2 = [], []
    res1 = con.execute('select* from passenger where mail=(?) and psw=(?);', (m2, p2))
    for i in res1:
        l1.append(i)
    print(l1)
    n = i[0]  # name in passenger table
    res2 = con.execute('select* from tkt_booked where name=(?);', (n,))
    for j in res2:
        l2.append(j)
    print(l2)
    res3 = con.execute('select* from train where tno=(?);', (j[0],))
    for k in res3:
        l2.append(k)

    lab = Label(ff, text='Train Ticket', font=('Arial', 25, 'bold'), bg='blue', fg='white', width=80, height=3).place(
        x=0, y=0)
    lab = Label(ff, text='Train Name', font=('Arial', 18, 'bold'), fg='blue', bg='white').place(x=100, y=200)
    lab = Label(ff, text=':   ' + k[3], font=('Arial', 18, 'bold'), fg='blue', bg='white').place(x=300, y=200)
    lab = Label(ff, text='Train Number', font=('Arial', 18, 'bold'), fg='blue', bg='white').place(x=600, y=200)
    lab = Label(ff, text=':   ' + str(k[2]), font=('Arial', 18, 'bold'), fg='blue', bg='white').place(x=750, y=200)
    lab = Label(ff, text='class', font=('Arial', 18, 'bold'), fg='blue', bg='white').place(x=900, y=200)
    lab = Label(ff, text=':   ' + (j[5]), font=('Arial', 18, 'bold'), fg='blue', bg='white').place(x=1000, y=200)

    lab = Label(ff, text='Name', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100, y=300)
    lab = Label(ff, text=':   ' + i[0], font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=300, y=300)
    lab = Label(ff, text='Mail', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100, y=330)
    lab = Label(ff, text=':   ' + i[1], font=('Arial', 12), fg='black', bg='white').place(x=300, y=330)
    lab = Label(ff, text='Adhar No', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100, y=360)
    lab = Label(ff, text=':   ' + i[3], font=('Arial', 12), fg='black', bg='white').place(x=300, y=360)
    lab = Label(ff, text='Contact No', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100, y=390)
    lab = Label(ff, text=':   ' + str(i[4]), font=('Arial', 12), fg='black', bg='white').place(x=300, y=390)
    lab = Label(ff, text='Gender', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100, y=420)
    lab = Label(ff, text=':   ' + j[3], font=('Arial', 12), fg='black', bg='white').place(x=300, y=420)
    # lab=Label(ff,text=i[3],font=('Arial',12,'bold'),fg='white',bg='brown').place(x=300,y=360)
    # lab=Label(ff,text=i[6],font=('Arial',12,'bold'),fg='white',bg='brown').place(x=300,y=550)  date
    lab = Label(ff, text='Age', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100, y=450)
    lab = Label(ff, text=':   ' + str(j[2]), font=('Arial', 12), fg='black', bg='white').place(x=300, y=450)
    lab = Label(ff, text='Total no of seat reserved', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=100,
                                                                                                                y=480)
    lab = Label(ff, text=':   ' + '1', font=('Arial', 12), fg='black', bg='white').place(x=300, y=480)
    no = randint(1, 100)
    lab = Label(ff, text='Seat No', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=300)
    lab = Label(ff, text=':   ' + str(no), font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=750, y=300)
    lab = Label(ff, text='From', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=330)
    lab = Label(ff, text=':   ' + k[0], font=('Arial', 12), fg='black', bg='white').place(x=750, y=330)
    lab = Label(ff, text='TO', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=360)
    lab = Label(ff, text=':   ' + k[1], font=('Arial', 12), fg='black', bg='white').place(x=750, y=360)
    lab = Label(ff, text='Traveling Date', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=390)
    lab = Label(ff, text=':   ' + k[4], font=('Arial', 12), fg='black', bg='white').place(x=750, y=390)
    lab = Label(ff, text='Arrival Time', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=420)
    lab = Label(ff, text=':   ' + k[5], font=('Arial', 12), fg='black', bg='white').place(x=750, y=420)
    # lab=Label(ff,text=i[3],font=('Arial',12,'bold'),fg='white',bg='brown').place(x=300,y=360)
    # lab=Label(ff,text=i[6],font=('Arial',12,'bold'),fg='white',bg='brown').place(x=300,y=550)  date
    lab = Label(ff, text='Reaching Time', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=450)
    lab = Label(ff, text=':   ' + k[6], font=('Arial', 12), fg='black', bg='white').place(x=750, y=450)

    lab = Label(ff, text='Paid Amount', font=('Arial', 12, 'bold'), fg='black', bg='white').place(x=600, y=480)
    lab = Label(ff, text=':   ' + str(k[7]), font=('Arial', 12), fg='black', bg='white').place(x=750, y=480)

    Button(ff, text='Print', bg='blue', fg='white', activebackground='brown', activeforeground='black', height=1,
           font=('Arial', 15, 'bold')).place(x=1000, y=400)
    ff.tkraise()


def change_password(ff):
    m, cp, np1, np2 = mail_up.get(), cur_psw.get(), new_psw1.get(), new_psw2.get()
    con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
    res = con.execute('select mail,psw from passenger;')
    ll1, ll2 = [], []
    for i in res:
        ll1.append(i[0])
        ll2.append(i[1])
    if np1 != np2:
        l = Label(fpsw, text='No matching password', font=('Arial', 20, 'bold'), fg='brown', bg='white', width=30,
                  height=3)
        l.place(x=600, y=600)

    if m not in ll1 or cp not in ll2:
        l = Label(fpsw, text='invalid mail or password', font=('Arial', 20, 'bold'), fg='brown', bg='white', width=30,
                  height=3)
        l.place(x=600, y=600)
    else:
        con.execute('update passenger set psw=(?) where mail=(?) and psw=(?);', (np2, m, cp))
        con.commit()
        l = Label(fpsw, text='updated password succsufully', font=('Arial', 20, 'bold'), fg='brown', bg='white',
                  width=30, height=3)
        l.place(x=600, y=600)
    con.close()


def logout(ff):
    m1 = m_logout.get()
    p1 = psw_logout.get()
    print(m1, p1)
    if m1 != '' or p1 != '':
        con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
        '''
        res=con.execute('select mail,psw from passenger;')
        ll1,ll2=[],[]
        for i in res:
            ll1.append(i[0])
            ll2.append(i[1])
        print(m1,ll1,p1,ll2)
        '''
        m2 = mail_log.get()
        p2 = psw_log.get()
        print(m1, m2, p1, p2)
        if m1 == m2 and p1 == p2:

            con.execute('delete from passenger where mail=(?) and psw=(?);', (m1, p1))
            con.commit()
            con.close()
            l = Label(flogout, text="removed your account", bg='white', fg='brown', font=('arial', 15, 'bold'),
                      width=30)
            l.place(x=700, y=350)
        else:
            l = Label(flogout, text="invalid mail or password", bg='white', fg='black', font=('arial', 15, 'bold'),
                      width=30)
            l.place(x=700, y=350)
    else:
        l = Label(flogout, text="Fill the field", bg='white', fg='black', font=('arial', 15, 'bold'), width=30)
        l.place(x=700, y=350)


# login function
def login(ff):
    m = mail_log.get()
    p = psw_log.get()
    con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
    if m != '' and p != '':
        res1 = con.execute('select mail from passenger;')
        res2 = con.execute('select mail,psw from passenger where mail=(?);', (m,))
        list1 = []
        for i in res1:
            list1.append(i)
        for k in res2:
            print(k)
        if m not in list1:
            l = Label(fl, text='invalid mail', font=('Arial', 20, 'bold'), fg='red', bg='white', width=20)
            l.place(x=600, y=300)
        if k[1] != p:
            l = Label(fl, text='wrong password', font=('Arial', 20, 'bold'), fg='red', bg='white', width=20)
            l.place(x=600, y=300)
        if k[0] == m and k[1] == p:
            l = Label(fl, text='', font=('Arial', 20, 'bold'), fg='red', bg='white', width=20)
            l.place(x=600, y=300)
            # sleep(100)
            frm(ff)
    elif m == '' or p == '':
        l = Label(fl, text='Fill all the fields', font=('Arial', 20, 'bold'), fg='red', bg='white', width=20)
        l.place(x=600, y=300)
    con.close()


# searching function

def search(ff):
    z = 0

    s = '_'
    for i in range(30):
        s += '_'
    lab = Label(fsrch, text=s, font=('Arial', 20, 'bold'), fg='black', bg='white').place(x=50, y=150)
    lab = Label(fsrch, text='Available Trains', font=('Arial', 30, 'bold'), fg='black', bg='white').place(x=50, y=120)
    lab = Label(fsrch, text='Note :', font=('Arial', 12), fg='white', bg='black').place(x=550, y=120)
    lab = Label(fsrch, text='( Booking Train number will be required for further process )', font=('Arial', 12, 'bold'),
                fg='black', bg='white').place(x=600, y=120)

    # getting fromcity and tocity name
    fc = (fromcity.get()).lower()
    tc = (tocity.get()).lower()
    dt = date.get()
    if fc != '' and tc != '' and dt != '':
        # l=Label(fsrch,text='',font=('Arial',30,'bold'),fg='lightgreen',bg='white',width=30)
        print(fc, tc)
        con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
        res = con.execute(
            "select tno,tname,arr_time,dep_time,amt,tdate from train where fromcity=(?) and tocity=(?) and tdate=(?);",
            (fc, tc, dt))
        yl = 250
        ct = 0
        z = 0
        ll = []
        for i in res:

            ct += 1
            print(i)
            ll.append(i)
            yl += 50

            l = Label(fsrch, text=i[1], font=('Arial', 12, 'bold'), fg='black', bg='white')
            l.place(x=500, y=yl)
            t_name = i[1]
            yl += 20
            l = Label(fsrch, text='Train Number :' + str(i[0]), font=('Arial', 10), fg='black', bg='white')
            t_num = i[0]
            l.place(x=500, y=yl)
            yl += 20
            l = Label(fsrch, text='FROM ' + fc + ' TO ' + tc, font=('Arial', 10), fg='black', bg='white')
            l.place(x=500, y=yl)
            yl += 20
            l = Label(fsrch, text='Amount :' + str(i[4]) + ' /person', font=('Arial', 10), fg='black', bg='white')
            l.place(x=500, y=yl)
            t_amt = i[4]
            yl += 20
            l = Label(fsrch, text='Date :' + dt, font=('Arial', 10), fg='black', bg='white')
            l.place(x=500, y=yl)
            # z+=1
            b = Button(fsrch, text='Booking', bg='brown', fg='white', activebackground='brown',
                       activeforeground='yellow', font=('Arial', 15), command=lambda: tck_book(ftbk))
            b.place(x=650, y=yl - 10)
            ss = '_'
            for i in range(20):
                ss += '____'
            yl += 18
            l = Label(fsrch, text=ss, font=('Arial', 20), fg='brown', bg='white')
            l.place(x=200, y=yl)

        if ct == 0:
            if fc not in res or tc not in res or dt not in res:
                l = Label(fsrch, text='Trains are not avaible......', font=('Arial', 30, 'bold'), fg='lightgreen',
                          bg='white', width=30)
                l.place(x=300, y=300)
        con.close()
        ff.tkraise()
    elif fc == '' or tc == '' or dt == '':
        l = Label(fs, text='Fill all the feilds', font=('Arial', 20), fg='black', bg='white', width=30)
        l.place(x=800, y=300)


def register(ff):
    n = name.get()
    m = mail.get()
    p = psw.get()
    mob = phone.get()
    a = adh.get()
    gen1 = g.get()  # 1-mail 2-femail
    gen = ''
    if gen1 == 1:
        gen = 'Mail'
    else:
        gen = 'Femail'
    d1, m1, y1 = str(dd.get()), str(mm.get()), str(yy.get())
    ag = age.get()
    print(n, m, p, mob, a, gen, d1, m1, y1, ag)

    if n == '' or m == '' or p == '' or a == '' or gen == '':
        l = Label(fr, text='Fill all the fields', font=('Arial', 20, 'bold'), fg='brown', bg='white', width=30,
                  height=1)
        l.place(x=700, y=200)
    if n != '' and m != '' and p != '' and mob != 0 and a != '' and gen != '' and ag != 0:
        con = sqlite3.connect('C:/Users/Aishwarya Patil/Desktop/DB/trainDB4.db')
        con.execute('insert into passenger values(?,?,?,?,?,?,?,?);',
                    (n, m, p, a, mob, gen, (d1) + '/' + (m1) + '/' + (y1), ag))
        con.commit()
        header = Label(ff, text='', font=('Arial', 20, 'bold'), fg='white', bg='brown', width=1500, height=3)
        header.place(x=0, y=0)
        header1 = Label(ff, text='Online reservation\nsystem', font=('Arial', 30, 'bold'), fg='white', bg='brown')
        header1.place(x=100, y=0)
        homeb = Button(ff, text='Home', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                       height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(f))
        homeb.place(x=700, y=20)
        searchb = Button(ff, text='Search', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                         height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(fs))
        searchb.place(x=800, y=20)
        loginb = Button(ff, text='Login', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                        height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(fl))
        loginb.place(x=900, y=20)
        regb = Button(ff, text='Register', bg='brown', fg='white', activebackground='brown', activeforeground='red',
                      height=1, width=8, font=('Arial', 15, 'bold'), command=lambda: frm(fr))
        regb.place(x=1000, y=20)
        l = Label(ff, text='congratulations!!!\nYou are registered succussfully', font=('Arial', 20, 'bold'),
                  fg='green', bg='white', width=30, height=3)
        l.place(x=100, y=100)
        ff.tkraise()


def reset(f):
    if f == fs:
        fromcity = Entry(fs, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        fromcity.place(x=250, y=350)
        tocity = Entry(fs, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        tocity.place(x=250, y=400)
        date = Entry(fs, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        date.place(x=250, y=450)
    elif f == fr:
        name = Entry(fr, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        name.place(x=250, y=300)
        mail = Entry(fr, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        mail.place(x=250, y=350)
        psw = Entry(fr, width=30, bg='white', fg='black', font=('arial', 15, 'bold'), show='.')
        psw.place(x=250, y=400)
        psw = Entry(fr, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        psw.place(x=290, y=450)
        adh = Entry(fr, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        adh.place(x=950, y=300)
        g = IntVar()
        gen = Label(fr, text="Gender", bg='white', fg='black', font=('arial', 14, 'bold'))
        gen.place(x=800, y=350)
        gender = Radiobutton(fr, text='Male', bg='white', fg='brown', variable=g, value=1).place(x=950, y=350)
        gender = Radiobutton(fr, text='Female', bg='white', fg='brown', variable=g, value=2).place(x=1000, y=350)
        d, m, y = IntVar(), IntVar(), IntVar()
        dob = Label(fr, text="Date of Birth\n(dd/mm/yy)", bg='white', fg='black', font=('arial', 14, 'bold'))
        dob.place(x=800, y=400)
        dd = Spinbox(fr, from_=1, to=31, bg='white', fg='black', textvariable=d, width=5).place(x=950, y=400)
        mm = Spinbox(fr, from_=1, to=12, bg='white', fg='black', textvariable=m, width=5).place(x=1000, y=400)
        yy = Spinbox(fr, from_=1990, to=2030, bg='white', fg='black', textvariable=y, width=5).place(x=1050, y=400)
        '''
        add=Label(fr,text="Address 1",bg='white',fg='black',font=('arial',14,'bold'))
        add.place(x=100,y=650)
        add=Entry(fr,width=30,bg='white',fg='black',font=('arial',15,'bold'))
        add.place(x=250,y=650)
        '''
        age = Label(fr, text="Age", bg='white', fg='black', font=('arial', 14, 'bold'))
        age.place(x=800, y=450)
        age = Entry(fr, width=30, bg='white', fg='black', font=('arial', 15, 'bold'))
        age.place(x=950, y=450)