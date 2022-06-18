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

    data=[('sugarpops','egbudom','chidindu','raphael','male','raph@gmail.com','08091516236','chidindu1',0),
          ('jet','egbudom','chidera','jude','male','jtegbudom@gmail.com','09012345667','123',0),
          ('rianne','egbudom','chidinma','maryann','female','maegbudom@gmail.com','083848284829','123',0),
          ('momo','egbudom','nneoma','marylyn','female','lyn.egbudom@gmail.com','09394822323','123',0),
          ('charley','egbudom','okeychukwu','charles','male','charlesegbudom@gmail.com','08035761160','123',0),
          ('jayne','egbudom','anayochukwu','janice','female','jegbudom@gmail.com','08088080767','123',0)]
    c.executemany("INSERT INTO customer_info(username, lastname, middlename, firstname, gender, email, phonenumber, password,type) VALUES(?,?,?,?,?,?,?,?,?)",data)

    #TRAINS
    c.execute("""CREATE TABLE IF NOT EXISTS trains(
                     train_id VARCHAR NOT NULL PRIMARY KEY,
                     name VARCHAR NOT NULL,
                     first_class_capacity INTEGER NOT NULL DEFAULT 0,
                     business_class capacity INTEGER NOT NULL DEFAULT 0,
                     regular_coach capacity INTEGER NOT NULL DEFAULT 0
                    )""")

    data=[( 'TIR-1001', 'Train 101', 24, 40, 88),
          ('TIR-1002', 'Train 102', 30, 40, 50),
          ('TIR-1003', 'Train 103', 30, 50, 92),
          ('TIR-1004', 'Train 104', 12, 50, 70),
          ('TIR-1005', 'Train 105', 20, 45, 70)]
    c.executemany("INSERT INTO trains(train_id, name, first_class_capacity, business_class, regular_coach) VALUES(?,?,?,?,?)",data)

    #SCHEDULES
    c.execute("""CREATE TABLE IF NOT EXISTS schedule(
                     schedule_id VARCHAR NOT NULL PRIMARY KEY,
                     train_id VARCHAR NOT NULL,
                     dep_location VARCHAR NOT NULL,
                     arr_location VARCHAR NOT NULL,
                     date VARCHAR NULL,
                     time VARCHAR NOT NULL,
                     type INTEGER check(type in (1,2)) NOT NULL DEFAULT 1,
                     first_class_price INTEGER NOT NULL DEFAULT 0,
                     business_class_price INTEGER NOT NULL DEFAULT 0,
                     regular_coach_price INTEGER NOT NULL DEFAULT 0,
                     FOREIGN KEY(train_id) REFERENCES customer_info(train_id)
                    )""")

    data=[('202201-0001', 'TIR-1001', 'Mobolaji Johnson Station', 'Babatunde Raji Fashola Station', None, '07:00:00', 1, 3000, 2000, 1000),
          ('202201-0003', 'TIR-1002', 'Wole Soyinka Station', 'Samuel Ladoke Akintola Station', '2022/01/07', '08:00:00', 2, 3500, 2500, 1500),
          ('202201-0002', 'TIR-1003', 'Samuel Ladoke Akintola Station', 'Obafemi Awolowo Station', None, '08:30:00', 1, 3000, 1700, 1000),
          ('202201-0004', 'TIR-1004', 'Mobolaji Johnson Station', 'Obafemi Awolowo Station', None, '00:00:00', 1, 6000, 4500, 3000),
          ('202201-0005', 'TIR-1004', 'Obafemi Awolowo Station', 'Mobolaji Johnson Station', None, '20:00:00', 1, 6000,4500, 3000),
          ('202201-0006', 'TIR-1004', 'Mobolaji Johnson Station', 'Obafemi Awolowo Station', None, '05:00:00', 1, 6000,4500, 3000),
          ('202201-0007', 'TIR-1004', 'Mobolaji Johnson Station', 'Obafemi Awolowo Station', None, '19:45:00', 1, 6000,4500, 3000),
          ('202201-0008', 'TIR-1002', 'Mobolaji Johnson Station', 'Babatunde Raji Fashola Station', None, '18:00:00', 1,3000, 2000, 1000),
          ('202201-0009', 'TIR-1004', 'Obafemi Awolowo Station', 'Mobolaji Johnson Station', None, '15:30:00', 1, 6000,4500, 3000)]
    c.executemany("INSERT INTO schedule VALUES(?,?,?,?,?,?,?,?,?,?)",data)

    # TICKET DATA
    c.execute("""CREATE TABLE IF NOT EXISTS tickets(
                     ticket_num VARCHAR NOT NULL PRIMARY KEY,
                     seat_num VARCHAR NOT NULL UNIQUE,
                     schedule_id VARCHAR NOT NULL,
                     p_name VARCHAR NOT NULL,
                     dep_date VARCHAR NOT NULL,
                     dep_time VARCHAR NOT NULL,
                     class VARCHAR check(class in ('first class', 'business class', 'regular coach')) NOT NULL,
                     username VARCHAR NOT NULL,
                     FOREIGN KEY(username) REFERENCES customer_info(username),
                     FOREIGN KEY(schedule_id) REFERENCES customer_info(schedule_id)
                    )""")

    data=[('12205A','FC-1','202201-0001','egbudom raphael','2022/01/07','08:00:00','first class','sugarpops'),
          ('22205B', 'BC-1', '202201-0001', 'egbudom jude', '2022/01/07', '08:00:00', 'business class', 'jet'),
          ('32205C', 'RC-1', '202201-0001', 'egbudom maryann', '2022/01/07', '08:00:00', 'regular coach', 'rianne'),
          ('42205D', 'FC-2', '202201-0001', 'egbudom marylyn', '2022/01/07', '08:00:00', 'first class', 'marylyn')]
    c.executemany("INSERT INTO tickets VALUES(?,?,?,?,?,?,?,?)",data)


    conn.commit()
    c.close()
    conn.close()

CreateDatabase()