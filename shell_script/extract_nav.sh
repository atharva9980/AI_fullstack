#!/bin/bash


curl -s https://www.amfiindia.com/spages/NAVAll.txt -o navdata.txt


awk -F ";" 'NF >= 4 && $1 ~ /^[0-9]+$/ { 
    gsub(/^[ \t]+|[ \t]+$/, "", $3); 
    gsub(/^[ \t]+|[ \t]+$/, "", $4); 
    print $3 "\t" $4 
}' navdata.txt > scheme_nav.tsv

echo "Extracted Scheme Name and NAV into scheme_nav.tsv"
