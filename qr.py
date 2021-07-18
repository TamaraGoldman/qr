# устанавливаем Pillow для обработки изображений: 
pip install pillow

# устанавливаем нужный модуль:
pip install qrcode[pil]

# создаем QR-код:
import qrcode
image = qrcode.make('https://github.com/TamaraGoldman')
image.save('qr_tg.png')