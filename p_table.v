`timescale 1ns / 1ps
module p_table(output reg [32:1] P_out, input [32:1] in);
  integer P[32:1];
  integer i;
  always @(*) begin
    P[1]=16;  P[2]=7;   P[3]=20;  P[4]=21;  P[5]=29;  P[6]=12;  P[7]=28;  P[8]=17;
    P[9]=1;   P[10]=15; P[11]=23; P[12]=26; P[13]=5;  P[14]=18; P[15]=31; P[16]=10;
    P[17]=2;  P[18]=8;  P[19]=24; P[20]=14; P[21]=32; P[22]=27; P[23]=3;  P[24]=9;
    P[25]=19; P[26]=13; P[27]=30; P[28]=6;  P[29]=22; P[30]=11; P[31]=4;  P[32]=25;
    for(i=1; i<=32; i=i+1)
      P_out[32-i+1] = in[32-P[i]+1];
  end
endmodule
