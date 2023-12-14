#!/bin/sh

NEW_PATH="zh-cn/handbook"


for document in $NEW_PATH/*; do

	echo $document
	python3 mc_translate.py --input $document --output $document

done	
