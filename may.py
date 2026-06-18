from flask import Flask, jsonify, render_template
import psycopg2

app = Flask(__name__)  # Conectar la bdd con flask 

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="Escuela", 
        user="postgres",
        password="12345"
    )

@app.route("/")
def inicio():
    # Conectar a la base de datos
    conexion = obtener_conexion()
    
    # Crear cursor
    cursor = conexion.cursor()
    
    # Ejecutar consulta
    cursor.execute("SELECT * FROM estudiantes")
    
    # Extraer los datos desde el cursor
    estudiantes = cursor.fetchall()
    
    # Cerrar el cursor
    cursor.close()
    
    # Cerrar la conexion a la bdd
    conexion.close()
    
    # Convertir a formato JSON
    lista_estudiantes = []
    
    # Recorrer la lista de estudiantes de la consulta
    for estudiante in estudiantes:
        lista_estudiantes.append({
            "id": estudiante[0],
            "nombre": estudiante[1],
            "edad": estudiante[2]
        })
        
    return jsonify(lista_estudiantes)
#Ruta de lunes
@app.route("/lunes")
def lunes():
   
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Lunes")
    Lunes = cursor.fetchall()
    cursor.close()
    conexion.close()
    actividades_lunes = []
    for Lista in Lunes:
        actividades_lunes.append({
            "id": Lista[0],
            "actividad": Lista[1]
        })
        
    return jsonify(actividades_lunes)
@app.route("/Martes")
def Martes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("Select * from Marte")
    Martes=cursor.fetchall()
    cursor.close()
    conexion.close()
    actividades_Marte=[]
    for Litsa2 in Martes:
        actividades_Marte.append({
        "id":Litsa2[0],
        "actividad":Litsa2[1]
        })
        return jsonify(actividades_Marte)
@app.route("/Miercoles")
def Miercoles ():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("select * from Miercoles")
        Miercoles= cursor.fetchall()
        cursor.close()
        conexion.close()
        actividades_Miercoles=[]
        for Lista3 in Miercoles:
          actividades_Miercoles.append({
            "id":Lista3[0],
            "actividades":Lista3[1]
            })
          return jsonify(actividades_Miercoles)
    

# Al final de todo archivo .py principal (TOTALMENTE AL BORDE IZQUIERDO)
if __name__ == "__main__":
    app.run(debug=True, port=8000)