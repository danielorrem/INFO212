from pathlib import Path
import qrcode

BASE_DIR = Path(__file__).parent.parent.resolve()

img = qrcode.make('qr code data')
img.save(BASE_DIR/'images'/'qr_image.png')