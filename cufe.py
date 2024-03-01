import requests
from bs4 import BeautifulSoup


def consultar_factura_por_cufe(cufe):
    url = f"https://dgi-fep.mef.gob.pa/Consultas/FacturasPorCUFE?CUFE={cufe}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        if "FECHA AUTORIZACIÓN" in soup.get_text():
            print("La respuesta contiene la palabra 'FECHA AUTORIZACIÓN'")
        else:
            print("La respuesta NO contiene la palabra 'FECHA AUTORIZACIÓN'")
    else:
        print("Error al consultar la URL")


# Ejemplo de uso
cufe_valor = "FE0620000000574-14-102616-7000002024022100801373190020110245789123"
consultar_factura_por_cufe(cufe_valor)
