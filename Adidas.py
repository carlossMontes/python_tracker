import Mensajero
import time
import AdidasChecador

tiempo = 60 * 60
liga = ['https://www.adidas.mx/tenis-lite-racer-2.0-rbn/FW3890.html',
        'https://www.adidas.mx/sandalias-adilette-aqua/F35543.html?pr=home_rr&slot=2']
precio = [1300, 500]

while True:
    for i in range(len(liga)):
        datos = AdidasChecador.check_price(liga[i], precio[i])
        title = datos[1]
        deseado = datos[9]
        price = datos[2]
        if(datos[0] == True):
            Mensajero.send_mail(liga[i], price, title.encode(
                encoding="ascii", errors="replace"))
        else:
            print('Revisando...', title, '//', deseado)
            print('Actual: ', price)
            print(datos[3], '/', datos[4], '/', datos[5], '-',
                  datos[6], ':', datos[7], ':', datos[8])
    time.sleep(tiempo)
