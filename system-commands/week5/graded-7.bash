total = 0;
for i in `echo ${number_arr[@]}`; do
	if (( $i%2 == 0 )); then
		total=$(($total+$i));
	fi;
done;
echo $total;

