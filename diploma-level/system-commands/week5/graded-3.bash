min=$1;
max=$2;
for i in $*; do
	if [ $i -gt $max ]; then
		max=$i;
	fi;
	if [ $i -lt $min ]; then
		min=$i;	
	fi;
done;
echo "Maximum: ${max} | Minimum: ${min}";

