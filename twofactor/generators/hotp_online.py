#!/usr/bin/env python3

""" Genera un QR HOTP compatible con Google Authenticator """

import webbrowser
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import HOTP

google_url = 'http://chart.googleapis.com/chart?chs=200x200&chld=M|0&cht=qr&chl='
cuenta = 'hotp@python-vigo.es'
expedido_por = None
key = b'abcdefghij'

hotp = HOTP(key, 6, SHA1(), backend=default_backend())
uri = hotp.get_provisioning_uri(cuenta, 0, expedido_por)
url = '%s%s' % (google_url, uri)
webbrowser.open(url)


