import mysql.connector
import csv

# Función para obtener datos de la tabla datos_usuario
def obtener_datos():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='195.179.238.58',  # Cambia por la dirección de tu servidor MySQL
            database='u927419088_testing_sql',  # Cambia por el nombre de tu base de datos
            user='u927419088_admin',  # Cambia por tu usuario de MySQL
            password='#Admin12345#'  # Cambia por tu contraseña de MySQL
        )
        cursor = conexion.cursor()

        # Consulta SQL para obtener los datos de la tabla datos_usuario
        query = "SELECT * FROM datos_usuario"
        cursor.execute(query)
        resultados = cursor.fetchall()

        # Obtener los nombres de las columnas
        nombres_columnas = [i[0] for i in cursor.description]

        return nombres_columnas, resultados

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función para exportar datos a CSV
def exportar_a_csv(nombres_columnas, resultados, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            # Escribir los nombres de las columnas
            escritor_csv.writerow(nombres_columnas)

            # Escribir los datos
            escritor_csv.writerows(resultados)

        print(f"Datos exportados exitosamente a {nombre_archivo}")

    except IOError as e:
        print(f"Error al escribir en el archivo CSV: {e}")

# Obtener datos de la tabla datos_usuario
nombres_columnas, resultados = obtener_datos()

# Exportar los datos obtenidos a un archivo CSV
nombre_archivo = 'snapshot_datos_usuario.csv'
exportar_a_csv(nombres_columnas, resultados, nombre_archivo)