import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gmy"
)


def Conexion(Sentencia):
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(Sentencia)
    except mysql.connector.Error as err:
        print(err)
    return cursor


