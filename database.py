import sqlite3

def CreateDatabase():
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()

    # CUSTOMER INFORMATION
    c.execute("""CREATE TABLE IF NOT EXISTS customer_info(
                     username VARCHAR NOT NULL PRIMARY KEY,
                     lastname VARCHAR NOT NULL,
                     middlename VARCHAR NOT NULL,
                     firstname VARCHAR NOT NULL,
                     gender TEXT check(gender in ('male', 'female', 'other')) NOT NULL,
                     email VARCHAR NOT NULL,
                     phonenumber VARCHAR NOT NULL,
                     password VARCHAR NOT NULL,
                     type INTEGER check(type in (0,1)) NOT NULL DEFAULT 0,
                     card_num VARCHAR,
                     exp_month VARCHAR,
                     exp_year VARCHAR,
                     card_holder VARCHAR,
                     card_code VARCHAR
                    )""")


    #TRAINS
    c.execute("""CREATE TABLE IF NOT EXISTS trains(
                     train_id VARCHAR NOT NULL PRIMARY KEY,
                     name VARCHAR NOT NULL,
                     first_class_capacity INTEGER NOT NULL DEFAULT 0,
                     business_class capacity INTEGER NOT NULL DEFAULT 0,
                     regular_coach capacity INTEGER NOT NULL DEFAULT 0
                    )""")
    #SCHEDULES
    c.execute("""CREATE TABLE IF NOT EXISTS schedule(
                     schedule_id VARCHAR NOT NULL PRIMARY KEY,
                     train_id VARCHAR NOT NULL,
                     dep_location VARCHAR NOT NULL,
                     arr_location VARCHAR NOT NULL,
                     date VARCHAR NOT NULL,
                     time VARCHAR check(time in ('8:00AM', '4:00PM')) NOT NULL,
                     first_class_price INTEGER NOT NULL DEFAULT 0,
                     business_class_price INTEGER NOT NULL DEFAULT 0,
                     regular_coach_price INTEGER NOT NULL DEFAULT 0,
                     FOREIGN KEY(train_id) REFERENCES customer_info(train_id)
                    )""")

    # TICKET DATA
    c.execute("""CREATE TABLE IF NOT EXISTS tickets(
                     ticket_num VARCHAR NOT NULL PRIMARY KEY,
                     seat_num VARCHAR NOT NULL,
                     schedule_id VARCHAR NOT NULL,
                     p_name VARCHAR NOT NULL,
                     p_mail VARCHAR NOT NULL,
                     p_phone VARCHAR NOT NULL,
                     dep_location VARCHAR NOT NULL,
                     arr_location VARCHAR NOT NULL,
                     dep_date VARCHAR NOT NULL,
                     dep_time VARCHAR check(dep_time in ('8:00AM', '4:00PM')) NOT NULL,
                     class VARCHAR check(class in ('first class', 'business class', 'regular coach')) NOT NULL,
                     username VARCHAR NOT NULL,
                     price VARCHAR NOT NULL DEFAULT 0,
                     FOREIGN KEY(username) REFERENCES customer_info(username),
                     FOREIGN KEY(schedule_id) REFERENCES customer_info(schedule_id)
                    )""")

    data=['sugarpops','egbudom','chidindu','raphael','male','raph@gmail.com','08091516236','chidindu1',0]
    c.execute("INSERT INTO customer_info(username, lastname, middlename, firstname, gender, email, phonenumber, password,type) VALUES(?,?,?,?,?,?,?,?,?)",data)
    conn.commit()
    c.close()
    conn.close()

CreateDatabase()