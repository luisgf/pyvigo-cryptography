#!/usr/bin/env python3

""" Genera un QR TOTP compatible con Google Authenticator """

import qrcode
import qrcode.image.svg

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP

cuenta = 'totp@python-vigo.es'
expedida_por = None
key = b'abcdefghij'

totp = TOTP(key, 6, SHA1(), 30, backend=default_backend())
uri = totp.get_provisioning_uri(cuenta, expedida_por)

img = qrcode.make(uri, image_factory=qrcode.image.svg.SvgImage)

with open('qr_totp.svg','wb') as f:
   img.save(f)

print('QR Generado')

