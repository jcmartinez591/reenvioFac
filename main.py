import requests
import pyodbc
import json

# Conexión a la base de datos
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER;DATABASE=;UID=hnladmin;PWD=')

# Consulta SQL para recuperar el valor del Payload
query = """
    SELECT Payload
FROM MDL11.tblElectronicInvoice WHERE Response_Code = '0260' and status =1 and einvoicestatus = 2
"""

# Ejecutar la consulta y recuperar los resultados
cursor = connection.cursor()
cursor.execute(query)
rows = cursor.fetchall()
connection.close()

# Realizar la solicitud HTTP POST con la cadena JSON como carga útil
url = "https://apim.aludra.cloud/mdl18/feRecepFEDGI"
headers = {
    'api-key': '',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
for row in rows:
    data = row[0]  # Convertir la fila en un diccionario
    payload_json = json.loads(row.Payload)
    payload_modificado = json.dumps(payload_json) # Convertir el diccionario a una cadena JSON
    response = requests.post(url, headers=headers, data=payload_modificado)  # Realizar la solicitud HTTP POST
    print(response.text)
