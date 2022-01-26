grep -o 'New session.*user [[:alnum:]]*' myauth.log | cut -d " " -f 6 | sort | uniq;
