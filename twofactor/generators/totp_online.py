#!/usr/bin/env python3

""" Genera un QR TOTP compatible con Google Authenticator """

import webbrowser
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP

google_url = 'http://chart.googleapis.com/chart?chs=200x200&chld=M|0&cht=qr&chl='
cuenta = 'totp@python-vigo.es'
expedida_por = None
key = b'abcdefghij'

totp = TOTP(key, 8, SHA1(), 30, backend=default_backend())
uri = totp.get_provisioning_uri(cuenta, expedida_por)
url = '%s%s' % (google_url, uri)
webbrowser.open(url)

