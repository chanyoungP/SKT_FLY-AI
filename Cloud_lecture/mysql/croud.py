import os
import mysql.connector 
from mysql.connector import  errorcode

config = {
    'host':'mysql-cy99-db.mysql.database.azure.com',
    'user':'chanchan',
    'password':'cksdudcksdud1!',
    'database':'sample_db',
    'client_flags':[mysql.connector.ClientFlag.SSL],
    'ssl_ca':"C:/Users/SSL/DigiCertGlobalRootCA.crt.pem"}

try:
    conn = mysql.connector.connect(**config)
    print("connection status good")
except mysql.connector.Error as E:
    if E.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("check your password")
    elif E.errno == errorcode.ER_BAD_DB_ERROR:
        print("DATABASE is not exist")
    else:
        print("ERROR")


cursor = conn.cursor()
prompt = '''
CREATE TABLE sample_db.book(
    title VARCHAR(50),
    author VARCHAR(50),
    publisher VARCHAR(40)
);
'''
cursor.execute(prompt)
print("create book table")

cursor.execute("ALTER TABLE sample_db.book CONVERT TO CHARSET utf8mb4;")
print("good modif table")


command = '''
INSERT INTO book (title, author, publisher) 
VALUES
("마케팅 불변 법칙","김민준","SKT"),
('abcdef','박찬영','나무위키');

'''
cursor.execute(command)
print("good adding value")


# result = cursor.fetchall()  # 혹은 fetchone()

conn.commit()
cursor.close()

