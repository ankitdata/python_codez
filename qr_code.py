'''
To generate QR code of any public access link
'''

import qrcode

source = 'https://your-public-link/'
qr_filename = 'qr.png'

img = qrcode.make(source)
img.save(qr_filename)
