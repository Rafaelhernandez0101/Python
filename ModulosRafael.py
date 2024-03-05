# main.py

from ConexionMySQLPythonRafael import MySQLDatabase
from ClaseAprendizRafael import Aprendiz

db = MySQLDatabase(
    host="localhost",
    username="root",
    password="",
    database="RafaelPython"
)
db.connect()

while True:
    print('\n')
    print("por favor ingrese la info del aprendiz (digite 'n' para salir): ")
    id = input("por favor ingrese numero de identificacion: ")
    if id.lower() == "n":
        break
    name = input("por favor ingres su nombre: ")
    surfname = input("por favor ingrese su apellido/S: ")
    email = input("digite su email: ")
    phone = input("por favor ingresar su numero: ")
    clas = input("por favor digite su ficha: ")

    nuevo = Aprendiz(id, name, surfname, phone, email, clas)
    nuevo.insert_into_db(db) 


aprendices = aprendiz.select_all_from_db(db)
for aprendiz in aprendices:
    a = Aprendiz(aprendiz[0], aprendiz[1], aprendiz[2], aprendiz[3], aprendiz[4], aprendiz[5])
    data = a.print_datos()
    print("\nInformacion del aprendiz")
    for clave, valor in data.items():
        print(f"{clave}: {valor}")

db.disconnect()