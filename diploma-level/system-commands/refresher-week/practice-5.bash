grep 'student on pts/4' myauth.log | grep -E -o 'to [[:alnum:]]+' | cut -d " " -f 2;
