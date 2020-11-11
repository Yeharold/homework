#!/bin/bash
res=$(ps -aux|grep -e "python3 .*/homework/app.py"|grep -v grep|awk '{print $2}');
for i in $res
do 
	kill -9 $i;
done
echo "shutdown homework server";
