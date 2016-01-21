#!/usr/bin/env python3


""" 
    Implementación de un validador de Tokens HOTP 

    RFC-4226 HMAC-Based One-time Password (HOTP)
"""

import os
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.twofactor.hotp import HOTP, InvalidToken
from cryptography.hazmat.primitives.hashes import SHA1

key = b'abcdefghij'
hotp = HOTP(key, 6, SHA1(), backend=default_backend())
token = input("Introduce Token: ").encode('utf-8')
valido = False

for counter in range(0, 100):
   try:
       hotp.verify(token, counter)
       valido = True
   except InvalidToken:
       pass


if valido:
   print("Token Válido")
else:
   print("Token Inválido")


