print('Inicializando scraping...')

import requests
from bs4 import BeautifulSoup

# URL de ejemplo para InfoJobs (puedes cambiarla según sea necesario)
URL_INFOJOBS_ESPECIFICO = "https://www.infojobs.net/parla/preparador-pedidos-textil-h-m-x-turno-noche-30-horas-l-d-illescas/of-i87b7672a834d5d92a7340b79cf400b?applicationOrigin=search-new&page=1&sortBy=PUBLICATION_DATE"

# Simular una petición desde un navegador con un User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


# Hacer la petición HTTP a la página
response = requests.get(URL_INFOJOBS_ESPECIFICO, headers=headers)

# Verificamos si la solicitud fue exitosa o si dio un error
if response.status_code == 200:
    print('Acceso exitoso a la página')
    
    # Parsear el HTML de la página con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # La fuente de la que obtenemos los datos.
    resource = "InfoJobs"
    
    # Intentar extraer el título del trabajo
    job_title = URL_INFOJOBS_ESPECIFICO.split('/')[-2].replace('-', ' ').title() 

    # Imprimir la fuente de datos
    print(f"Fuente de datos: {resource}")
    
    # Imprimir el título del trabajo
    print(f"Descriptivo Titulo: {job_title}")
else:
    print(f'Error al acceder a la página: {response.status_code}')


api_response= requests.get("https://api.infojobs.net/api/9/offer")
print(api_response)
