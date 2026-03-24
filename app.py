import streamlit as st
from Crypto.Cipher import DES
import binascii

st.title("DES Encryption (Hex Input)")

st.write("Enter 16-hex-digit plaintext and key (64-bit)")

plaintext_hex = st.text_input("Plaintext")
key_hex = st.text_input("Key (HEX)", "133457799BBCDFF1")


def hex_to_bin(hex_string):
    return bin(int(hex_string,16))[2:].zfill(64)


if st.button("Encrypt"):

    if len(plaintext_hex) != 16 or len(key_hex) != 16:
        st.error("Plaintext and Key must be 16 hex characters (64 bits)")
    else:

        plaintext = bytes.fromhex(plaintext_hex)
        key = bytes.fromhex(key_hex)

        cipher = DES.new(key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)

        ciphertext_hex = binascii.hexlify(ciphertext).decode().upper()

        st.write("Plaintext Binary")
        st.code(hex_to_bin(plaintext_hex))

        st.write("Key Binary")
        st.code(hex_to_bin(key_hex))

        st.write("Ciphertext (HEX)")
        st.success(ciphertext_hex)
