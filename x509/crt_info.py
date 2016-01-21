#!/usr/bin/env python3

"""
    Ejemplo de lectura de datos contenidos en un certificado x509.
    Devuelve un objecto de tipo "Certificate".

"""

from binascii import hexlify
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

pem_data = open('pyvigo.crt','rb').read()
cert = x509.load_pem_x509_certificate(pem_data, default_backend())

print("Versión:\t%s" % cert.version)
print("Numero de Serie:\t%s" % cert.serial)
print("SHA256 Fingerprint:\t%s" % hexlify(cert.fingerprint(hashes.SHA256())).decode())
print("Fecha Inicio validez:\t%s" % str(cert.not_valid_before))
print("Fecha Fin validez:\t%s" % str(cert.not_valid_after))
print("Emisor:")
print("\t", cert.issuer.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME)[0].value)
print("\t", cert.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value)

print("Subject:")
print("\t", cert.subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME)[0].value)
print("\t", cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value)
print("\t", cert.subject.get_attributes_for_oid(x509.NameOID.EMAIL_ADDRESS)[0].value)


print("Algoritmo de firma: %s" % cert.signature_hash_algorithm.name)


