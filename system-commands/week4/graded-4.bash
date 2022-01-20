lower=(`ls | grep '[a-z0-9]\{10\}'`);
upper=(`ls | grep -v '[a-z0-9]\{10\}'`);
