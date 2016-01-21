#!/usr/bin/env python3

from cryptography.fernet import Fernet

def main():
   """ Implementación de Fernet """

   key = Fernet.generate_key()   # Generamos una clave aleatoria
   f = Fernet(key)

   # Cifrado del mensaje
   criptograma = cifra(f, b"Python Vigo, Cryptography. Mensaje de prueba.")
   print("\nToken: %s\n" % criptograma.decode('utf-8'))

   # Descifrado
   print("Mensaje: %s\n" % descifra(f, criptograma).decode('utf-8'))

def cifra(f, mensaje):
    return f.encrypt(mensaje)

def descifra(f, criptograma):
    return f.decrypt(criptograma)

if __name__ == '__main__':
   main()


