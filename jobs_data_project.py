print('Inicializando scriping...')

import requests
from bs4 import BeautifulSoup

#EJEMPLO DE URL DE INFOJOBS. POR FILTRO ESPAÑA Y MAS RECIENTES. 
URL_INFOJOBS= "https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=&segmentId=&page=1&sortBy=PUBLICATION_DATE&onlyForeignCountry=false&countryIds=17&sinceDate=_24_HOURS&salaryMin=6000&salaryPeriod=YEAR&salaryType=GROSS"

#----------------------------------------------------
# DES DE LA PAGINA PRINCIPAL NO PODEMOS OBTENER LA INFO DEL EMPLEO, TENDRIAMOS QUE ENTRAR PÁGINA POR PAGINA. POR PÁGINA TENEMOS 20 EMPLEOS + 2 PATROCINADO.
# VEMOS UN EJEMPLO CON LA PÁGINA DE DENTRO DE UN EMPLEO. 
#----------------------------------------------------

URL_INFOJOBS_ESPECIFICO= "https://www.infojobs.net/burgos/tecnico-reparacion-h-m-k-tuin-tiendas-apple-burgos/of-i533ef83dda4b4da436ac8a17030ec0?applicationOrigin=search-new&page=1&sortBy=PUBLICATION_DATE"

# Simular una petición desde un navegador con un User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Hacer la petición HTTP a la página
response = requests.get(URL_INFOJOBS_ESPECIFICO, headers=headers)

#Verificamos si la solicitud fue exitosa o si dio un error
if response.status_code== 200:
    print(f'Acceso exitoso a la página')
    #Parsear el HTML de la página con BeautifulSoup
    soup= BeautifulSoup(response.text, 'html.parser')

    #Imprimir el título de la página para ver si funciona. 
    print(f"Título de la página: {soup.title.text}")
else:
    print(f'Error al acceder a la página: {response.status_code}')


