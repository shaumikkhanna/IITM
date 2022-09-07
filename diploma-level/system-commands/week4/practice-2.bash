var=`grep "${pin}" Pincode_info.csv | cut -d "," -f 1,4`;
var=`echo ${var/'Circle,'/}`;
echo ${var/'Division'/};
