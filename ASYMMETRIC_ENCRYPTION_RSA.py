#!/bin/python3

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes



if __name__ == "__main__":
  
    
    # Create a private key 
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
  
    p = private_key.private_numbers().p
    q = private_key.private_numbers().q
    print(f"p: {p}")
    print(f"q: {q}")

    # Create public key 
    public_key = private_key.public_key()

    n = public_key.public_numbers().n 
    e = public_key.public_numbers().e 

    print(f"n: {n}")
    print(f"e: {e}")

    # Encryption with public key 
    message = b"Encryption using Asymmetric with RSA"
    message_padding = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    cipher_text = public_key.encrypt(message, message_padding)

    print(f"plain_text: {message}")
    print(f"ciphertext: {cipher_text}")

    # Decryption with private key
    message_unpadding = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    plain_text = private_key.decrypt(cipher_text, message_unpadding)
    print(f"plaintext: {plain_text}")


"""
private_key.private_numbers(): This method returns an object containing the private numbers of the RSA key, including the prime factors p and q.
p and q: In RSA, the private key is generated using two large prime numbers, p and q. These numbers are kept secret and are crucial for the security of the RSA algorithm.

private_key.public_key(): This method derives the public key from the private key. In RSA, the public key is generated using the modulus n (calculated as p * q) and the public exponent e
n: The modulus n is the product of the two prime numbers p and q (n = p * q). It's a part of both the public and private keys.
e: The public exponent e is a key parameter used for encrypting messages. In this case, e is typically set to 65537, as specified during the private key generation.