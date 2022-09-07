if [ -r $1 -a ! -w $1 -a ! -x $1 ]; then
	echo Yes;
fi;

