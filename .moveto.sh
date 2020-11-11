#!/bin/bash
if [ ! -d ~/homework/$1 ];then 
  mkdir ~/homework/$1
else
  echo "failed,$1 exists"
fi
mv ~/homework/static ~/homework/$1/$(date +"%Y%m%d")
mkdir ~/homework/static
echo "seccussfully move to $1"
