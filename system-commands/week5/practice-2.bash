total=0;
for hash in `cat result`; do
	filename=`grep "$hash" map | cut -d " " -f 2`;
	amt=`cat $filename | head -n 1 | cut -d "$" -f 2`;
	total=$(($total+$amt));
done;
echo $total;

