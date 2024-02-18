import mysql.connector

conexion = mysql.connector.connect(host="localhost", user="root", passwd="root", auth_plugin='mysql_native_password')

cursor = conexion.cursor()

def create_db():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS CBLosPalacios;")
        cursor.execute("USE CBLosPalacios;")
        print("Se creo la base de datos \n")

    except:
        print("Error al crear base de datos\n")

def create_table():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios" 
        "(nombre varchar(100) NOT NULL,"
        "email varchar(100) NOT NULL,"
        "password varchar(300) NOT NULL,"
        "PRIMARY KEY (email));")
        
        sql_create_table = """
            CREATE TABLE IF NOT EXISTS Encargos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                articulo VARCHAR(100) NOT NULL,
                talla VARCHAR(100),
                email VARCHAR(100) NOT NULL,
                FOREIGN KEY (email) REFERENCES Usuarios(email)
            )
        """
        cursor.execute(sql_create_table)

        print("Se creo la tabla usuarios \n")
    except:
        print("Error al crear la tabla usuarios \n")   

create_db()
create_table()