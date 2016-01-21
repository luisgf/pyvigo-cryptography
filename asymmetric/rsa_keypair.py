#!/usr/bin/env python3

"""
    Genera un par de claves RSA (privada y pública)
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

priv_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

priv_pem = priv_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
           )

print(priv_pem.decode())

pub_key = priv_key.public_key()

pub_pem = pub_key.public_bytes(
             encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo
          )
print(pub_pem.decode())

