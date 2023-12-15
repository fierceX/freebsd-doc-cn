#!/bin/sh

NEW_PATH="zh-cn/handbook"


for document in $(find "$NEW_PATH" -name "*.po" ); do

	echo $document
	python3 mc_translate.py --input $document --output $document --type chatgpt

done	
