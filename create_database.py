import sqlite3

conn = sqlite3.connect('train_reservation.db')
query = (''' CREATE TABLE CUSTOMERLOGIN
            (FULLNAME      TEXT   NOT NULL,
            EMAILADDRESS   TEXT  NOT NULL,
            USERNAME       TEXT  NOT NULL,
            PASSWORD       CHAR(50));
            ''')
conn.execute(query)
conn.close()




