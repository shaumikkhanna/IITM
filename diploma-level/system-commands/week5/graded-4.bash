for (( i=2; i<=$1/2; i++ )); do
	if (( $1%$i == 0 )); then
		exit 1;
	fi;
done;
echo Yes;

