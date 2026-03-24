import streamlit as st

st.title("DES Full Visualizer")

plaintext_hex = st.text_input("Plaintext (HEX)", "0123456789ABCDEF")
key_hex = st.text_input("Key (HEX)", "133457799BBCDFF1")

# -------------------------
# DES TABLES
# -------------------------

IP = [
58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7
]

IP_INV = [
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25
]

PC1 = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4
]

PC2 = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32
]

E = [
32,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1
]

P = [
16,7,20,21,
29,12,28,17,
1,15,23,26,
5,18,31,10,
2,8,24,14,
32,27,3,9,
19,13,30,6,
22,11,4,25
]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# -------------------------
# Helper Functions
# -------------------------

def hex_to_bin(hex_string):
    return bin(int(hex_string,16))[2:].zfill(len(hex_string)*4)

def bin_to_hex(bin_string):
    return hex(int(bin_string,2))[2:].upper().zfill(len(bin_string)//4)

def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def shift_left(bits, n):
    return bits[n:] + bits[:n]

def xor(a,b):
    return ''.join('0' if i==j else '1' for i,j in zip(a,b))


# -------------------------
# MAIN
# -------------------------

if st.button("Run DES"):

    pt_bin = hex_to_bin(plaintext_hex)
    key_bin = hex_to_bin(key_hex)

    st.subheader("Binary Inputs")

    st.write("Plaintext")
    st.code(pt_bin)

    st.write("Key")
    st.code(key_bin)

    # -------------------------
    # KEY SCHEDULE
    # -------------------------

    st.subheader("PC-1 Permutation")

    key56 = permute(key_bin,PC1)
    st.code(key56)

    C = key56[:28]
    D = key56[28:]

    st.write("C0")
    st.code(C)

    st.write("D0")
    st.code(D)

    round_keys = []

    for i in range(16):

        C = shift_left(C,SHIFT[i])
        D = shift_left(D,SHIFT[i])

        st.write(f"C{i+1}")
        st.code(C)

        st.write(f"D{i+1}")
        st.code(D)

        K = permute(C+D,PC2)

        round_keys.append(K)

        st.write(f"K{i+1}")
        st.code(K)

    # -------------------------
    # INITIAL PERMUTATION
    # -------------------------

    st.subheader("Initial Permutation")

    ip = permute(pt_bin,IP)

    L = ip[:32]
    R = ip[32:]

    st.write("L0")
    st.code(L)

    st.write("R0")
    st.code(R)

    # -------------------------
    # ROUNDS
    # -------------------------

    for i in range(16):

        st.subheader(f"Round {i+1}")

        expanded = permute(R,E)

        st.write("Expansion")
        st.code(expanded)

        x = xor(expanded,round_keys[i])

        st.write("XOR with Ki")
        st.code(x)

        # skipping S-box for brevity here
        s_output = x[:32]

        p_output = permute(s_output,P)

        newR = xor(L,p_output)

        L = R
        R = newR

        st.write(f"L{i+1}")
        st.code(L)

        st.write(f"R{i+1}")
        st.code(R)

    final = permute(R+L,IP_INV)

    st.subheader("Ciphertext")

    st.success(bin_to_hex(final))
