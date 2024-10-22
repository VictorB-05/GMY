import mysql.connector

class Conexion:
    SERVIDOR = 'localhost'
    USUARIO = 'root'
    CONTRASENA = ''
    BASE_DATOS = 'gmy'

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host=self.SERVIDOR,
            user=self.USUARIO,
            password=self.CONTRASENA,
            database=self.BASE_DATOS
        ) #Se crea la conexión
        self.cursor = self.conexion.cursor() #Y a partir de ella, el cursor, que es el que ejecuta las consultas sobre la BD

    def getCursor(self):
        return self.cursor

    def close(self):
        self.cursor.close()
        self.conexion.close()

    def commit(self):
        self.conexion.commit()
