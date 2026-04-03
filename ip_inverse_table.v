`timescale 1ns / 1ps
module ip_inverse_table(output reg [64:1] IP_inv_out, input [64:1] in);
  integer IP_inverse[64:1];
  integer i;
  always @(*) begin
    IP_inverse[1]=40;  IP_inverse[2]=8;   IP_inverse[3]=48;  IP_inverse[4]=16;
    IP_inverse[5]=56;  IP_inverse[6]=24;  IP_inverse[7]=64;  IP_inverse[8]=32;
    IP_inverse[9]=39;  IP_inverse[10]=7;  IP_inverse[11]=47; IP_inverse[12]=15;
    IP_inverse[13]=55; IP_inverse[14]=23; IP_inverse[15]=63; IP_inverse[16]=31;
    IP_inverse[17]=38; IP_inverse[18]=6;  IP_inverse[19]=46; IP_inverse[20]=14;
    IP_inverse[21]=54; IP_inverse[22]=22; IP_inverse[23]=62; IP_inverse[24]=30;
    IP_inverse[25]=37; IP_inverse[26]=5;  IP_inverse[27]=45; IP_inverse[28]=13;
    IP_inverse[29]=53; IP_inverse[30]=21; IP_inverse[31]=61; IP_inverse[32]=29;
    IP_inverse[33]=36; IP_inverse[34]=4;  IP_inverse[35]=44; IP_inverse[36]=12;
    IP_inverse[37]=52; IP_inverse[38]=20; IP_inverse[39]=60; IP_inverse[40]=28;
    IP_inverse[41]=35; IP_inverse[42]=3;  IP_inverse[43]=43; IP_inverse[44]=11;
    IP_inverse[45]=51; IP_inverse[46]=19; IP_inverse[47]=59; IP_inverse[48]=27;
    IP_inverse[49]=34; IP_inverse[50]=2;  IP_inverse[51]=42; IP_inverse[52]=10;
    IP_inverse[53]=50; IP_inverse[54]=18; IP_inverse[55]=58; IP_inverse[56]=26;
    IP_inverse[57]=33; IP_inverse[58]=1;  IP_inverse[59]=41; IP_inverse[60]=9;
    IP_inverse[61]=49; IP_inverse[62]=17; IP_inverse[63]=57; IP_inverse[64]=25;
    for(i=1; i<=64; i=i+1)
      IP_inv_out[64-i+1] = in[64-IP_inverse[i]+1];
  end
endmodule
