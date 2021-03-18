""" Aqui se coloca todo lo que hace el modulo a que contexto el corresponde """

__author__ = "Carlos Alberto Montes Romero"
__copyright__ = "Copyright 2019, UTNG"
__credits__ = "Codigo Facilito, Dev Ed"

__licence__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Carlos Montes"
__email__ = "carloss.montes@gmail.com"
__status__ = "Development"

import csv
import requests
import smtplib
import time
from bs4 import BeautifulSoup
from datetime import datetime

# Necesarios para conseguir el titulo y precio del proyecto. Buscar por User-Agent
headers = {
    "User-Agent":  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.50'}

# Funcion para monitorear precio. Se necesita la URL del producto de ML y el precio que se busca


def check_price(liga, deseado):

    # Se consigue el codigo HTML de la pagina
    page = requests.get(liga, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Se consigue el titulo a traves de la clase marcada, se extrae el texto del array
    h1 = soup.findAll("h1", {"class": "ui-pdp-title"})
    h1 = h1[0].get_text()
    title = h1

    # Se consigue el precio a traves de la clase marcada, se extrae el texto del array y se convierte a numero
    # Cambian constantemente la estructura, revisar que trae el precio correcto
    formato = soup.findAll("span", {"class": "price-tag-fraction"})
    if(len(formato) == 3):
        strPrecio = formato[1].get_text()
    else:
        strPrecio = formato[0].get_text()

    buscar = ","
    reemplazar = ""
    strPrecio = strPrecio.replace(buscar, reemplazar)
    precio = int(strPrecio)

    fecha = datetime.now()

    # Si el precio del articulo es igual o menor al deseado
    esMenor = False
    if(precio <= deseado):
        esMenor = True

    # Escribe los datos en un archivo cvs
    # Nombre del archivo, lo crea o lo abre para escribir en la ultima linea, nueva linea
    with open('ML_mycsv.csv', 'a', newline='') as f:
        tw = csv.writer(f)
        tw.writerow([title, precio, deseado, datetime.now()])

    #       0           1   2       3           4               5           6           7           8           9
    return esMenor, title, precio, fecha.day, fecha.month, fecha.year, fecha.hour, fecha.minute, fecha.second, deseado
