`timescale 1ns / 1ps
module processkey_des(
  output reg [48:1] key1,  key2,  key3,  key4,
  output reg [48:1] key5,  key6,  key7,  key8,
  output reg [48:1] key9,  key10, key11, key12,
  output reg [48:1] key13, key14, key15, key16,
  input [64:1] key
);
  wire [56:1] PC1_out;
  wire [48:1] PC2_out;

  pc1_table PC1M (.PC1_out(PC1_out), .in(key));

  reg [28:1] C[16:0], D[16:0];
  reg [48:1] K[1:16];
  reg [56:1] CD;
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
      CD = {C[i], D[i]};
      // inline PC2 permutation
      begin : pc2_block
        integer PC2[48:1]; integer k;
        PC2[1]=14;  PC2[2]=17;  PC2[3]=11;  PC2[4]=24;  PC2[5]=1;   PC2[6]=5;
        PC2[7]=3;   PC2[8]=28;  PC2[9]=15;  PC2[10]=6;  PC2[11]=21; PC2[12]=10;
        PC2[13]=23; PC2[14]=19; PC2[15]=12; PC2[16]=4;  PC2[17]=26; PC2[18]=8;
        PC2[19]=16; PC2[20]=7;  PC2[21]=27; PC2[22]=20; PC2[23]=13; PC2[24]=2;
        PC2[25]=41; PC2[26]=52; PC2[27]=31; PC2[28]=37; PC2[29]=47; PC2[30]=55;
        PC2[31]=30; PC2[32]=40; PC2[33]=51; PC2[34]=45; PC2[35]=33; PC2[36]=48;
        PC2[37]=44; PC2[38]=49; PC2[39]=39; PC2[40]=56; PC2[41]=34; PC2[42]=53;
        PC2[43]=46; PC2[44]=42; PC2[45]=50; PC2[46]=36; PC2[47]=29; PC2[48]=32;
        for(k=1; k<=48; k=k+1)
          K[i][48-k+1] = CD[56-PC2[k]+1];
      end
    end

    key1=K[1];  key2=K[2];  key3=K[3];  key4=K[4];
    key5=K[5];  key6=K[6];  key7=K[7];  key8=K[8];
    key9=K[9];  key10=K[10];key11=K[11];key12=K[12];
    key13=K[13];key14=K[14];key15=K[15];key16=K[16];
  end
endmodule
