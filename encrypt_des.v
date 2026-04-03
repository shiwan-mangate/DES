`timescale 1ns / 1ps
module encrypt_des(
    output reg [64:1] ciphertext,
    input [64:1] message,
    input [64:1] key
);

wire [64:1] ip_msg;
wire [64:1] final_msg;

reg [32:1] L[16:0];
reg [32:1] R[16:0];

wire [48:1] key1,key2,key3,key4,key5,key6,key7,key8;
wire [48:1] key9,key10,key11,key12,key13,key14,key15,key16;

reg [48:1] K[16:1];

integer i;

processkey_des pk(
key1,key2,key3,key4,key5,key6,key7,key8,
key9,key10,key11,key12,key13,key14,key15,key16,
key
);

ip_table ip1(ip_msg, message);

always @(message)
begin

{L[0],R[0]} = ip_msg;

K[1]=key1; K[2]=key2; K[3]=key3; K[4]=key4;
K[5]=key5; K[6]=key6; K[7]=key7; K[8]=key8;
K[9]=key9; K[10]=key10; K[11]=key11; K[12]=key12;
K[13]=key13; K[14]=key14; K[15]=key15; K[16]=key16;

for(i=1;i<=16;i=i+1)
begin
    L[i] = R[i-1];
    R[i] = L[i-1] ^ f_function(R[i-1],K[i]);
end

end

ip_inverse_table ip2(final_msg,{R[16],L[16]});

always @(*)
ciphertext = final_msg;

endmodule
