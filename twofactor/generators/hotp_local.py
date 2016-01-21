#!/usr/bin/env python3

""" Genera un QR HOTP compatible con Google Authenticator """

import qrcode
import qrcode.image.svg

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import HOTP

cuenta = 'hotp@python-vigo.es'
expedido_por = None
key = b'abcdefghij'

hotp = HOTP(key, 6, SHA1(), backend=default_backend())
uri = hotp.get_provisioning_uri(cuenta, 0, expedido_por)
img = qrcode.make(uri, image_factory=qrcode.image.svg.SvgImage)

with open('qr_hotp.svg','wb') as f:
  img.save(f)


