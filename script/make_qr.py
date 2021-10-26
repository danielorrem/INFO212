import qrcode

img = qrcode.make('test')
img.save('qr_image.png')