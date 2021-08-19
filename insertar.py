# encoding: utf-8

import conexion

try:
    db = conexion.db

    cursor = db.cursor()
    sql = "INSERT INTO peliculas(titulo,anio) VALUES(%s,%s)" 
    val = ("sarasa",1992)
    cursor.execute(sql,val)
    db.commit()
    print("Consulta realizada correctamente")
    db.close()
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

