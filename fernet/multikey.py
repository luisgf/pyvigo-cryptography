#!/usr/bin/env python3

from cryptography.fernet import Fernet, MultiFernet, InvalidToken

def main():
   """ Implementación de Fernet con múltiples claves  """

   criptogramas = [b'gAAAAABWn0bMCZBZzJXXjTXxQRcvHyjc1PoHxy95MQdr50xUoy7V5Kyc0mqN1EvWMnAqGAbMw6rjaTP3MA6UvA_vSfw8OX6-STgKpgVc0M8U9wHt_3n89JQbIsXZrDiovsWpK-2f46Zl',b'gAAAAABWn0b_ztuZwaq1jx8rCeYh8-Btc5bea8X77HOnHH8F5nN3UfbXjf_Kvn_slVjOJSDEQ0Eq3ZP-EdUMkRF0jzZElxNQBw1MqZPI25Vr6Y2yYwYwG-jE4TnjAymOeTrYPFY0ckXC',b'gAAAAABWn0ca60xM4fxGyTK95rUhBdfEwnMBrTEKLhKJ3TlHVODpeP3nz8L4b_Ru2vzjbvaUzcauu-w8d3X9FdFf2vb1BmBbxvjrigdZUVsXizVbgen0-vRv7V6uzCotZr8bae_XlR56']

   """ Claves generadas anteriormente, cada clave es una cadena URL-safe
       codificada en base64 que contiene una cadena de 32 bytes """
  
   key1 = Fernet(b'qxzGyGJeqz6z3tNLLdDZqzkuZGCsTw9rgWYcohJgqyM=')
   key2 = Fernet(b'ed8o2q0mPgH1pczZVy_Bnn8NIHVlCMztwb81sY_gAfU=')
   f = MultiFernet([key1, key2])

   # Descifrado de Mensajes
   try:
       for criptograma in criptogramas:
           print("[+] Mensaje: %s" % descifra(f, criptograma).decode('utf-8'))

   except InvalidToken:
      print("[!] Error descifrando mensaje. Clave desconocida.")
      print("[!] Mensaje: %s " % criptograma.decode('utf-8'))

def descifra(f, criptograma):
    """ El descifrado es iterativo, se prueba todas las
        claves hasta dar con la buena, en caso contrario
        salta una excepcion de tipo InvalidToken """

    return f.decrypt(criptograma)


if __name__ == '__main__':
   main()


