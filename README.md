# Cryptography in Python

This repository contains Python scripts that demonstrate various cryptographic techniques, including RSA asymmetric encryption and AES symmetric encryption in different modes (CBC and ECB).

## Contents

1. **ASYMMETRIC_ENCRYPTION_RSA.py**
   - Demonstrates RSA encryption and decryption.
   - Generates an RSA key pair (private and public keys).
   - Encrypts and decrypts messages using the RSA algorithm.
   
2. **AES_CBC_MODE.py**
   - Demonstrates AES encryption and decryption in CBC (Cipher Block Chaining) mode.
   - Includes key generation and padding techniques.
   - Provides examples of encrypting and decrypting messages using AES in CBC mode.

3. **AES_ECB_MODE.py**
   - Demonstrates AES encryption and decryption in ECB (Electronic Codebook) mode.
   - Similar to the CBC mode script but uses ECB mode, which is less secure due to its lack of chaining.
   - Provides examples of encrypting and decrypting messages using AES in ECB mode.

## Requirements

To run these scripts, you need to have Python installed along with the following libraries:

- `cryptography`

You can install the required library using pip:

```bash
pip install cryptography
