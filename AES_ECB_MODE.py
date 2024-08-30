#!/bin/python3

import os
from cryptography.hazmat.primitives.ciphers import Cipher 
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB
from cryptography.hazmat.primitives import padding 

if __name__ == "__main__":
 #plaintext to kept confidentials
 plaintext = b"secret message to be tranfered"
 print(f"plaintext:{plaintext}")
 

 #256-bits AES Key
 key = os.urandom(256 // 8)

 #Create a ECB AES cipher
 aes_cipher=Cipher(AES(key),ECB())


 #Encryption 
 ciphertext = aes_cipher.encryptor().update(plaintext)
 print(f"Ciphertext:{ciphertext}")


 #Decryption
 recovery_plaintext = aes_cipher.decryptor().update(ciphertext)
 print(f"recovery plaintext:{recovery_plaintext}")

 """the output of above code is 
   plaintext:secret message to be tranfered
   Ciphertext:b'\x0c\x1e,\x00!\xb8m\xd4\x88S\xb8:\x7f\x13\xabC'
   recovery plaintext:b'secret message t'
    In above code it occur block size issue, In block cipher encryption (like AES in ECB mode), the message is divided into blocks of a fixed size (e.g., 16 bytes for AES). 
    If your message doesn’t exactly fit into these blocks, it might get cut off or not be fully decrypted.
    To ensure the message fits into blocks correctly, padding is often added to the plaintext before encryption.
    If the padding isn't handled correctly during decryption, you might only recover part of the original message."""


 #padding the plaintext 
 padder = padding.PKCS7(128).padder()  # AES uses 128-bit (16 bytes) blocks
 padded_plaintext = padder.update(plaintext) + padder.finalize()

  #Encryption 
 ciphertext = aes_cipher.encryptor().update(padded_plaintext)



 #Decryption
 recovery_plaintext = aes_cipher.decryptor().update(ciphertext)


 #Removing padding from the text 
 unpadder = padding.PKCS7(128).unpadder()
 recovery_data =unpadder.update(recovery_plaintext) + unpadder.finalize()
 print("---message after padding ---")
 print(f"recovery plaintext:{recovery_data}")

    






