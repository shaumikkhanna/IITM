while getopts "lwns" options; do
	case $options in
		l)
			echo "l chosen"
			;;
		w)
			echo "w chosen"
			;;
		n)
			echo "n chosen"
			;;
		s)
			echo "s chosen"
			;;
	esac;
done