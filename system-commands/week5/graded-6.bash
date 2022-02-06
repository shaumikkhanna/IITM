if ! [ -d $1 ]; then
	mkdir $1;
fi;

for filename in `ls perf_folder`; do
	if [[ $filename == *perf*\.c ]]; then
		echo $filename;
		mv perf_folder/$filename $1/program_$filename;
	fi;
done;

