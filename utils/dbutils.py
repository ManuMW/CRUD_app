import mysql.connector as mysql

def connectDb():
    return mysql.connect(host="localhost", user="root", password="root", database = 'words')

def createSchema():
    #sql0 = '''CREATE DATABASE IF NOT EXISTS words;'''
    sql = '''CREATE TABLE IF NOT EXISTS `words`.`input_word`(`id` INT NOT NULL AUTO_INCREMENT,
    `word` VARCHAR(100) NULL,
    PRIMARY KEY (`id`));'''

    connection = connectDb()
    cursor = connection.cursor()

    #cursor.execute(sql0)
    cursor.execute(sql)

    connection.commit()
    connection.close()

def writeToDb(cmd):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute(cmd)
    conn.commit()
    conn.close()

def readFromDb(cmd):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute(cmd)
    val = cur.fetchall()
    conn.close()
    return val

def updateDb(cmd):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute(cmd)
    conn.close()

def deleteFromDb(cmd):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute(cmd)
    conn.close()

createSchema()