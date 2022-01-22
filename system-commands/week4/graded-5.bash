grep -E "${state}" Pincode_info.csv | cut -d "," -f 5 | grep -E '(.).{4}\1' | wc -l;
