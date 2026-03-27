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
