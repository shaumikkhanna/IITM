grep 'New session.*user guest\.' myauth.log | tail -n 1 | cut -d " " -f 1-3;
