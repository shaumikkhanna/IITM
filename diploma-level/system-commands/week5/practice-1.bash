out="";
i=1;
for argument in "$@"; do
	if (( i%2 == 1 )); then
		out="$out $argument";
	fi;
	(( i++ ));
done;
echo $out
