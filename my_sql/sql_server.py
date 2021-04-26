import pymysql as msq
import psycopg2
DB_NAME='postgres'
DB_PASS='mahdi21376'
DB_USER='postgres'
DB_HOST='localhost'
def connect_to_database():
    con=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
    cursor = con.cursor()
    select_from_database(cursor,con)

def select_from_database(cursor,con):
    #com = "CREATE TABLE student (id SERIAL PRIMARY KEY , name VARCHAR);"
   # com ="INSERT INTO student (name) VALUES(%S)",("ali",)
    try:
        cursor.execute("SELECT * FROM test;")
        print(cursor.fetchall())
        con.commit()
    except:
        print('error')
        con.rollback()

    con.close()

if __name__ == '__main__':
    connect_to_database()
