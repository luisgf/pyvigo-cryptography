#!/usr/bin/env python3

"""
    Procesado de una lista CRL
"""

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

crl_pem = open('crl_der.crt','rb').read()
crl = x509.load_der_x509_crl(crl_pem, default_backend())

print("Numero de Certificados revocados: %d" % len(crl))

print("Serial\t\t\t\t\tFecha Revocación")
for cert in crl:
   print("%s\t%s" % (cert.serial_number, str(cert.revocation_date)))

