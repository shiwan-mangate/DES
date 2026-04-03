`timescale 1ns / 1ps
module ip_table(output reg [64:1] out, input [64:1] in);

integer IP[64:1];
integer i;

always @(*)
begin

IP[1]=58; IP[2]=50; IP[3]=42; IP[4]=34;
IP[5]=26; IP[6]=18; IP[7]=10; IP[8]=2;
...
IP[64]=7;

for(i=1;i<=64;i=i+1)
out[64-i+1] = in[64-IP[i]+1];

end

endmodule
