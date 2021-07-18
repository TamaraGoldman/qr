# устанавливаем Pillow для обработки изображений: 
# pip3 install pillow

# устанавливаем нужный модуль:
# pip3 install qrcode[pil]

# создаем QR-код:
import qrcode
image = qrcode.make('https://github.com/TamaraGoldman')
image.save('qr_tg.png')