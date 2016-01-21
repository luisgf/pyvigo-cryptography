#!/usr/bin/env python3


""" 
    Implementación de un sistema que valida tokens TOTP.

    Atención: Revisa cuidadosemente la hora del validador/Cliente.

    La mayoria de problemas con los tokens TOTP vienen por desfases
    temporales entre cliente y servidor

    RFC-6238 Time-based One-time Password (TOTP)
"""

import time
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.twofactor.totp import TOTP, InvalidToken
from cryptography.hazmat.primitives.hashes import SHA1

key = b'abcdefghij'
totp = TOTP(key, 6, SHA1(), 30, backend=default_backend())

token = input("Token?: ").encode()

try:
    totp.verify(token, time.time())
    print("Token Válido")
except InvalidToken:
    print("Token Inválido")

