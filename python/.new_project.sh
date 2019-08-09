#!/bin/bash
function init() {
	cd
	python3 create.py $1 $2 $3 $4
	cd /Users/neeraj/Desktop/$1
	git init
	git remote add origin https://github.com/neerajp99/$1.git
	git pull origin master
	subl .
}
