# DES Encryption and Decryption Algorithm

This repository contains an implementation of the Data Encryption Standard (DES) algorithm in Python. DES is a symmetric-key block cipher that encrypts and decrypts data in blocks of 64 bits using a 56-bit key.

## Overview

The DES algorithm consists of several steps, including:

- **Initial Permutation (IP)**: Rearranges the bits of the input plaintext.
- **Key Generation**: Generates 16 round keys from the initial 64-bit key.
- **Rounds**: Executes 16 rounds of permutation and substitution operations on the plaintext.
- **Final Permutation (FP)**: Reverses the initial permutation to produce the ciphertext.

This implementation supports both encryption and decryption of plaintext using the DES algorithm.

## Features

- Encrypt plaintext using a 64-bit hexadecimal input.
- Decrypt ciphertext using the same algorithm and key.
- Supports input and output in hexadecimal format.
- Provides clear function names and comments for easy understanding.
