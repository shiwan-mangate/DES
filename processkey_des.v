`timescale 1ns / 1ps
module processkey_des(
  output reg [48:1] key1,  key2,  key3,  key4,
  output reg [48:1] key5,  key6,  key7,  key8,
  output reg [48:1] key9,  key10, key11, key12,
  output reg [48:1] key13, key14, key15, key16,
  input [64:1] key
);
  wire [56:1] PC1_out;
  reg  [56:1] CD;
  wire [48:1] PC2_out;

  pc1_table PC1M (.PC1_out(PC1_out), .in(key));
  pc2_table PC2M (.PC2_out(PC2_out), .in(CD));

  reg [28:1] C[16:0], D[16:0];
  reg [48:1] K[1:16];
  integer i;
  integer shift_left[1:16];

  always @(key) begin
    shift_left[1]=1;  shift_left[2]=1;  shift_left[3]=2;  shift_left[4]=2;
    shift_left[5]=2;  shift_left[6]=2;  shift_left[7]=2;  shift_left[8]=2;
    shift_left[9]=1;  shift_left[10]=2; shift_left[11]=2; shift_left[12]=2;
    shift_left[13]=2; shift_left[14]=2; shift_left[15]=2; shift_left[16]=1;

    C[0] = PC1_out[56:29];
    D[0] = PC1_out[28:1];

    for(i=1; i<=16; i=i+1) begin
      if(shift_left[i] == 1) begin
        C[i] = {C[i-1][27:1], C[i-1][28]};
        D[i] = {D[i-1][27:1], D[i-1][28]};
      end else begin
        C[i] = {C[i-1][26:1], C[i-1][28:27]};
        D[i] = {D[i-1][26:1], D[i-1][28:27]};
      end
      CD   = {C[i], D[i]};
      K[i] = PC2_out;
    end

    key1=K[1];  key2=K[2];  key3=K[3];  key4=K[4];
    key5=K[5];  key6=K[6];  key7=K[7];  key8=K[8];
    key9=K[9];  key10=K[10];key11=K[11];key12=K[12];
    key13=K[13];key14=K[14];key15=K[15];key16=K[16];
  end
endmodule
