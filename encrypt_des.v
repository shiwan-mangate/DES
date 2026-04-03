`timescale 1ns / 1ps
module encrypt_des(output reg [64:1] ciphertext, input [64:1] message, input [64:1] key);

  wire [64:1] ip_out, ip_inv_out;
  wire [48:1] key1,key2,key3,key4,key5,key6,key7,key8;
  wire [48:1] key9,key10,key11,key12,key13,key14,key15,key16;

  reg  [64:1] ip_inv_in;
  reg  [32:1] L[16:0], R[16:0];
  reg  [48:1] K[16:1];
  wire [32:1] f_out[1:16];
  integer i;

  ip_table        IP_MOD  (.IP_out(ip_out),     .in(message));
  ip_inverse_table IPI_MOD (.IP_inv_out(ip_inv_out), .in(ip_inv_in));
  processkey_des  PK      (
    .key1(key1),   .key2(key2),   .key3(key3),   .key4(key4),
    .key5(key5),   .key6(key6),   .key7(key7),   .key8(key8),
    .key9(key9),   .key10(key10), .key11(key11), .key12(key12),
    .key13(key13), .key14(key14), .key15(key15), .key16(key16),
    .key(key)
  );

  genvar g;
  generate
    for(g=1; g<=16; g=g+1) begin : f_gen
      f_function FF (.f_out(f_out[g]), .R(R[g-1]), .K(K[g]));
    end
  endgenerate

  always @(message) begin
    {L[0], R[0]} = ip_out;

    K[1]=key1;  K[2]=key2;  K[3]=key3;  K[4]=key4;
    K[5]=key5;  K[6]=key6;  K[7]=key7;  K[8]=key8;
    K[9]=key9;  K[10]=key10;K[11]=key11;K[12]=key12;
    K[13]=key13;K[14]=key14;K[15]=key15;K[16]=key16;

    for(i=1; i<=16; i=i+1) begin
      L[i] = R[i-1];
      R[i] = L[i-1] ^ f_out[i];
    end

    ip_inv_in  = {R[16], L[16]};
    ciphertext = ip_inv_out;
  end
endmodule
