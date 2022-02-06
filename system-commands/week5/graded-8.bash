if [ $1 -eq 1 -o $1 -eq 8 ]; then
	echo SUNDAY;
elif [ $1 -eq 2 -o $1 -eq 9 ]; then
	echo MONDAY;
elif [ $1 -eq 3 ]; then
	echo TUESDAY;
elif [ $1 -eq 4 ]; then
	echo WEDNESDAY;
elif [ $1 -eq 5 ]; then
	echo THURSDAY;
elif [ $1 -eq 6 ]; then
	echo FRIDAY;
elif [ $1 -eq 7 ]; then
	echo SATURDAY;
else
	echo ERROR;
fi; 
