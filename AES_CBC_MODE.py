#!/bin/python3
import os
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives import padding

if __name__ == "__main__":
    plaintext = b"secret message to transfer"
    print(f"Plaintext: {plaintext}")

    # 256-bit AES key
    key = os.urandom(256 // 8)

    # 128-bit random initialization vector (IV) required for CBC mode of operation
    iv = os.urandom(16)

    # Create the cipher
    AES_cipher = Cipher(AES(key), CBC(iv))

    # Padding the plaintext
    padder = padding.PKCS7(128).padder()
    padded_text = padder.update(plaintext) + padder.finalize()

    # Encryption
    encryption_text = AES_cipher.encryptor().update(padded_text) + AES_cipher.encryptor().finalize()

    # Decryption
    decryption_text = AES_cipher.decryptor().update(encryption_text) + AES_cipher.decryptor().finalize()

    # Unpadding the text
    unpadder = padding.PKCS7(128).unpadder()
    recovery_data = unpadder.update(decryption_text) + unpadder.finalize()

    print(f"Recovery data: {recovery_data}")




