#!/bin/bash
echo "Script to setup a github repo for a technical book."
echo "Creating $1 subdirectories. 1 for each chapter. Pushing to Github."

for i in {1..$1}
do
	mkdir "ch$i"
done
git add .
git commit -m "Chapter Structure Created."
git branch -M main
git remote add origin $2
git push -u origin main
