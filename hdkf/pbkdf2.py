#!/usr/bin/env python3

""" Derivación de Clave usando el algoritmo PBKDF2 """

import base64
import os
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b'MiClaveInicial'
salt = os.urandom(16)   # No bloqueante

iteracion = 0
iteraciones_max = 10000000

while (iteracion < iteraciones_max):
   kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, 
                    salt=salt, iterations=iteracion, 
                    backend=default_backend())
   
   ts = time.time()
   key = base64.urlsafe_b64encode(kdf.derive(password))
   te = time.time()

   print("Iteración %d: %s %.2gs" % (iteracion, key.decode('utf-8'), te-ts))
   iteracion += 500000



