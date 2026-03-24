import streamlit as st
from Crypto.Cipher import DES
import binascii

st.title("DES 64-bit Encryption Visualizer")

st.write("DES works on a 64-bit block (8 characters).")

plaintext = st.text_input("Enter 8 Character Plaintext")
key = st.text_input("Enter 8 Character Key")

def to_bin(data):
    return ''.join(format(b,'08b') for b in data)

def split_lr(binary):
    return binary[:32], binary[32:]

if st.button("Encrypt"):

    if len(key) != 8 or len(plaintext) != 8:
        st.error("Plaintext and Key must both be exactly 8 characters (64 bits)")
    else:

        key_bytes = key.encode()
        pt_bytes = plaintext.encode()

        cipher = DES.new(key_bytes, DES.MODE_ECB)

        pt_bin = to_bin(pt_bytes)

        st.write("Plaintext Binary")
        st.code(pt_bin)

        L, R = split_lr(pt_bin)

        st.write("L0")
        st.code(L)

        st.write("R0")
        st.code(R)

        for i in range(1,17):

            st.subheader(f"Round {i}")

            newL = R

            xor_result = int(L,2) ^ int(R,2)
            newR = format(xor_result,'032b')

            st.write("Li = Ri-1")
            st.code(newL)

            st.write("Ri = Li-1 XOR Ri-1")
            st.code(newR)

            L = newL
            R = newR

        final = R + L

        st.write("Final Swap")
        st.code(final)

        ciphertext = cipher.encrypt(pt_bytes)

        st.write("Ciphertext (Hex)")
        st.code(binascii.hexlify(ciphertext).decode())
