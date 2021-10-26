import qrcode

img = qrcode.make('qr code data')
img.save('qr_image.png')