# encoding: utf-8
import mysql.connector

def conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='peliculas')
        print("Conexión correcta")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    return conexion

db = conexion()