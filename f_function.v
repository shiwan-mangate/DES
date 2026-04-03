`timescale 1ns / 1ps
module f_function(output reg [32:1] f_out, input [32:1] R, input [48:1] K);
  wire [48:1] E_out;
  wire [32:1] P_out;
  wire [4:1] s1_out, s2_out, s3_out, s4_out, s5_out, s6_out, s7_out, s8_out;
  reg  [48:1] xor_out;
  reg  [32:1] sbox_concat;

  e_table     ET  (.E_out(E_out), .in(R));
  sbox1       SB1 (.out(s1_out), .B(xor_out[48:43]));
  sbox2       SB2 (.out(s2_out), .B(xor_out[42:37]));
  sbox3       SB3 (.out(s3_out), .B(xor_out[36:31]));
  sbox4       SB4 (.out(s4_out), .B(xor_out[30:25]));
  sbox5       SB5 (.out(s5_out), .B(xor_out[24:19]));
  sbox6       SB6 (.out(s6_out), .B(xor_out[18:13]));
  sbox7       SB7 (.out(s7_out), .B(xor_out[12:7]));
  sbox8       SB8 (.out(s8_out), .B(xor_out[6:1]));
  p_table     PT  (.P_out(P_out), .in(sbox_concat));

  always @(*) begin
    xor_out    = K ^ E_out;
    sbox_concat = {s1_out, s2_out, s3_out, s4_out, s5_out, s6_out, s7_out, s8_out};
    f_out      = P_out;
  end
endmodule
