import Mensajero
import time
import MLChecador

tiempo = 60 * 60
liga = ['https://articulo.mercadolibre.com.mx/MLM-709362774-enchufe-inteligente-wifi-smart-plug-alexa-home-socket-_JM?searchVariation=42118015125&quantity=1&variation=42118015125#searchVariation=42118015125&position=1&type=item&tracking_id=c0004925-04db-4723-807f-d77ab693675b',
        'https://articulo.mercadolibre.com.mx/MLM-660276467-contacto-inteligente-wifi-app-led-smart-plug-socket-apagador-temporizador-google-home-alexa-celular-_JM?searchVariation=31818208786#searchVariation=31818208786&position=2&type=item&tracking_id=82d31657-9f0a-4439-a253-1b78c1250598',
        'https://articulo.mercadolibre.com.mx/MLM-794298516-pulsera-inteligente-xiaomi-mi-band-5-original-global-espanol-_JM?searchVariation=60039270260#searchVariation=60039270260&position=1&type=item&tracking_id=5aeb96a2-5119-469e-86ba-0c7b11d0c029',
        'https://articulo.mercadolibre.com.mx/MLM-729609436-aspiradora-robotica-inteligente-xiaomi-mijia-para-el-hogar-_JM#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f6a27989-2f99-4cae-bd8d-09c9c9b8041a',
        'https://www.mercadolibre.com.mx/aspiradora-koblenz-seco-mojado-wd-25k-95l-negra-y-verde/p/MLM8753445?searchVariation=MLM8753445&source=search#searchVariation=MLM8753445&position=1&type=product&tracking_id=01da30a0-f480-444f-85cb-3f7ab1c8f7d4',
        'https://www.mercadolibre.com.mx/xiaomi-redmi-note-9s-dual-sim-128-gb-glacier-white-6-gb-ram/p/MLM15586827?product_trigger_id=MLM15586824&quantity=1',
        'https://www.mercadolibre.com.mx/xiaomi-mi-tv-stick-mdz-24-aa-de-voz-full-hd-8gb-negro-con-memoria-ram-de-1gb/p/MLM15984003?pdp_filters=deal:MLM3684#searchVariation=MLM15984003&position=7&type=product&tracking_id=735f47c5-42d0-4b28-bfd0-21bca146604b'
        ]
precio = [140, 140, 750, 7000, 760, 5200, 780]

while True:
    for i in range(len(liga)):
        datos = MLChecador.check_price(liga[i], precio[i])
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
