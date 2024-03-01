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
    'api-key': 'FcKTfV8rBFmGI4/Gibk/dibdl0NPmfyjHFIFR7GaQxT7ScoC2OpHWsH626V2WFjfvY+UiR7caBDHdwJi6QaPEL+nRZIOG5A9FtXO5sP8n65KsypwM6nrg8twLqHGRwaF3BNIgXsV19tq0yE3zlhB2YVmRWkukLPpZS5Rh/wduHw2OMif8odtnDH5I2Bjhe0ev9WwRrSl6GdmMVd3Z8p2fWIrYAsLbLucbwmsAaldzd6tgQgpNmG85oLA2g07cASuUzCKW83Lb04OBwj1QukAPGbO+umCBraU7sD9dFO0vv/BijV7pDN6So7dYy4VE7z02jvcF4GCc49WQGPtLCVl/7yuhcNEWxnsHQAszIN5fYI=',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
for row in rows:
    data = row[0]  # Convertir la fila en un diccionario
    payload_json = json.loads(row.Payload)
    payload_modificado = json.dumps(payload_json) # Convertir el diccionario a una cadena JSON
    response = requests.post(url, headers=headers, data=payload_modificado)  # Realizar la solicitud HTTP POST
    print(response.text)
