import streamlit as st

# ── CYBER SECURITY DASHBOARD CSS ─────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* App background */
.stApp{
background: linear-gradient(135deg,#020617,#020617,#0f172a);
color:#e2e8f0;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#020617;
border-right:1px solid rgba(0,255,255,0.15);
}

/* Title */
h1{
color:#67e8f9;
letter-spacing:1px;
}

/* Cards */
.card{
background:rgba(15,23,42,0.6);
padding:20px;
border-radius:12px;
border:1px solid rgba(0,255,255,0.1);
box-shadow:0 0 20px rgba(0,255,255,0.08);
margin-bottom:20px;
backdrop-filter: blur(6px);
}

/* Stage Box */
.stage-box{
background:#020617;
border-left:4px solid #22c55e;
padding:15px;
border-radius:8px;
margin-bottom:15px;
}

/* Binary code display */
.binary-box{
background:#000000;
color:#22c55e;
font-family:monospace;
padding:12px;
border-radius:8px;
border:1px solid #1e293b;
}

/* Buttons */
.stButton>button{
background:linear-gradient(90deg,#06b6d4,#22c55e);
color:white;
border-radius:8px;
padding:10px 20px;
font-weight:600;
border:none;
transition:0.3s;
}

.stButton>button:hover{
box-shadow:0 0 12px #22c55e;
transform:translateY(-2px);
}

/* Inputs */
.stTextInput input{
background:#020617;
color:white;
border:1px solid rgba(0,255,255,0.15);
border-radius:6px;
}

/* Code blocks */
pre{
background:#000;
border:1px solid #1e293b;
border-radius:8px;
color:#22c55e;
}

/* Success message */
.stAlert{
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ── TITLE ───────────────────────────────────────────────────────────
st.title("DES Full Intermediate Visualizer")

plaintext_hex = st.text_input("Plaintext HEX", "0123456789ABCDEF")
key_hex       = st.text_input("Key HEX",       "133457799BBCDFF1")


# ── Tables ──────────────────────────────────────────────────────────
IP = [
58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7,
]

IP_INV = [
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25,
]

PC1 = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4,
]

PC2 = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32,
]

E = [
32,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1,
]

P = [
16,7,20,21,
29,12,28,17,
1,15,23,26,
5,18,31,10,
2,8,24,14,
32,27,3,9,
19,13,30,6,
22,11,4,25,
]
S = [
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
],
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
],
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
],
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
],
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
],
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
],
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
],
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
]
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# ── Helpers ─────────────────────────────────────────────────────────
def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a,b):
    return ''.join('1' if x!=y else '0' for x,y in zip(a,b))


# ── MAIN LOGIC (UNCHANGED) ───────────────────────────────────────────
if st.button("Run DES"):

    pt_bin  = bin(int(plaintext_hex,16))[2:].zfill(64)
    key_bin = bin(int(key_hex,16))[2:].zfill(64)

    st.subheader("Input")
    st.write("Plaintext Binary")
    st.code(pt_bin)

    st.write("Key Binary")
    st.code(key_bin)

    ip = permute(pt_bin,IP)

    L,R = ip[:32],ip[32:]

    st.subheader("Initial Permutation")
    st.code(ip)

    st.write("L0")
    st.code(L)

    st.write("R0")
    st.code(R)

    key56 = permute(key_bin,PC1)

    C,D = key56[:28],key56[28:]

    round_keys=[]

    for i in range(16):
        C = left_shift(C,SHIFTS[i])
        D = left_shift(D,SHIFTS[i])
        K = permute(C+D,PC2)
        round_keys.append(K)

    st.subheader("16 Feistel Rounds")

    for i in range(16):

        st.markdown(f"---\n### Round {i+1}")

        ER = permute(R,E)

        x = xor(ER,round_keys[i])

        s=""

        for j in range(8):

            chunk = x[j*6:(j+1)*6]

            row = int(chunk[0]+chunk[5],2)
            col = int(chunk[1:5],2)

            val = S[j][row][col]

            s += format(val,'04b')

        Fp = permute(s,P)

        new_R = xor(L,Fp)

        L,R = R,new_R

        st.write("Expansion")
        st.code(ER)

        st.write("XOR with key")
        st.code(x)

        st.write("Sbox")
        st.code(s)

        st.write("Permutation P")
        st.code(Fp)

        st.write("L")
        st.code(L)

        st.write("R")
        st.code(R)

    pre_final = R+L

    cipher_bin = permute(pre_final,IP_INV)

    cipher_hex = hex(int(cipher_bin,2))[2:].upper().zfill(16)

    st.subheader("Final Permutation")

    st.code(cipher_bin)

    st.success(f"Ciphertext (HEX): {cipher_hex}")
