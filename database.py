import sqlite3

def CreateDatabase():
    conn = sqlite3.connect('railly.db')
    c = conn.cursor()

    # CUSTOMER INFORMATION
    c.execute("""CREATE TABLE IF NOT EXISTS customer_info(
                     username VARCHAR NOT NULL PRIMARY KEY,
                     lastname VARCHAR NOT NULL,
                     middlename VARCHAR DEFAULT 0,
                     firstname VARCHAR NOT NULL,
                     email VARCHAR NOT NULL,
                     phonenumber VARCHAR NOT NULL,
                     password VARCHAR NOT NULL,
                     card_num VARCHAR,
                     exp_month VARCHAR,
                     exp_year VARCHAR,
                     card_holder VARCHAR,
                     card_code VARCHAR
                    )""")

    #STATION INFORMATION
    c.execute("""CREATE TABLE IF NOT EXISTS station_info(
                         station VARCHAR NOT NULL PRIMARY KEY,
                         morning_time VARCHAR NOT NULL,
                         evening_time VARCHAR NOT NULL,
                         going_distance VARCHAR NOT NULL,
                         return_distance VARCHAR NOT NULL
                        )""")
    #LAGOS-IBADAN TRAIN
    c.execute("""CREATE TABLE IF NOT EXISTS lagos(
                         date VARCHAR NOT NULL PRIMARY KEY,
                         time VARCHAR check(time in ('8:00AM', '4:00PM')) NOT NULL,
                         first_class INTEGER NOT NULL,
                         business_class INTEGER NOT NULL,
                         regular_coach INTEGER NOT NULL
                        )""")
    # IBADAN-LAGOS TRAIN
    c.execute("""CREATE TABLE IF NOT EXISTS ibadan(
                         date VARCHAR NOT NULL PRIMARY KEY,
                         time VARCHAR check(time in ('8:00AM', '4:00PM')) NOT NULL,
                         first_class INTEGER NOT NULL,
                         business_class INTEGER NOT NULL,
                         regular_coach INTEGER NOT NULL
                        )""")
    # TICKET DATA
    c.execute("""CREATE TABLE IF NOT EXISTS tickets(
                         ticket_num VARCHAR NOT NULL PRIMARY KEY,
                         p_name VARCHAR NOT NULL,
                         p_mail VARCHAR NOT NULL,
                         p_phone VARCHAR NOT NULL,
                         departure VARCHAR NOT NULL,
                         destination VARCHAR NOT NULL,
                         date VARCHAR NOT NULL,
                         dep_time VARCHAR check(dep_time in ('8:00AM', '4:00PM')) NOT NULL,
                         arr_time VARCHAR NOT NULL,
                         class VARCHAR check(class in ('FIRST CLASS', 'BUSINESS CLASS', 'REGULAR COACH')) NOT NULL,
                         username VARCHAR NOT NULL,
                         FOREIGN KEY(username) REFERENCES customer_info(username)
                        )""")
    conn.commit()
    c.close()
    conn.close()

CreateDatabase()