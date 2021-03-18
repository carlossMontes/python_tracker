""" Aqui se coloca todo lo que hace el modulo a que contexto el corresponde """

__author__ = "Carlos Alberto Montes Romero"
__copyright__ = "Copyright 2020, chaozwoah"
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

# Funcion que manda el email


def send_mail(liga, deseado, titulo):

    # Credenciales para ingresar a la cuenta
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Ingreso a la cuenta. Contraseña generada por Google Apps Password
    server.login('carloss.montes@gmail.com', 'kqvcsxuaosxvdxdm')

    # Generacion del correo. Incluye asunto, cuerpo. Se guarda en msg
    precio = str(deseado)
    title = titulo

    subject = "El precio de " + str(titulo) + \
        " ha disminuido a $" + str(precio) + "MXN"
    body = "Revisa el articulo de Mercado Libre " + \
        str(title) + " porque ha disminuido a $" + str(precio) + \
        "MXN \n Revisa el producto en la URL: " + str(liga)
    # body = "Revisa el articulo de Mercado Libre  porque ha disminuido a $MXN \n Revisa el producto en la URL: "
    msg = f"Subject: {subject}\n\n{body}"

    # Se envia el correo, necesita remitente, destinatario y mensaje
    server.sendmail(
        'carloss.montes@gmail.com',
        'carloss.montes@gmail.com',
        msg
    )

    # Avisa que se ha enviado el mensaje y cierra la conexion
    print('El email ha sido enviado\n')
    server.quit()
