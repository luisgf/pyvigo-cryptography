#!/usr/bin/env python3

from cryptography.fernet import Fernet, InvalidToken
from time import sleep

def main():
   """ Implementación de Fernet con expiración """

   key = Fernet.generate_key()
   f = Fernet(key)

   # Cifrado del mensaje
   criptograma = cifra(f, b"Python Vigo, Cryptography. Fernet con TTL")
   print("Token: %s " % criptograma.decode('utf-8'))

   for intento in range(0,2):
       # Descifrado
       try:
          print("Intento [%d]: %s" % (intento,descifra(f, criptograma, ttl=1).decode('utf-8')))
       except InvalidToken:
          print("Intento [%d] Error: Token Inválido. Expiró." % intento)
       finally:
          sleep(3)


def cifra(f, mensaje):
    return f.encrypt(mensaje)

def descifra(f, criptograma, ttl=None):
    """ Especificando un TTL conseguimos que salte una excepción
        de tipo InvalidToken si el mensaje ha sido generado hace
        más de 'ttl' segundos  """
    
    return f.decrypt(criptograma, ttl)


if __name__ == '__main__':
   main()


