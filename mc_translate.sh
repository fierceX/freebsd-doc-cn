#!/bin/sh

NEW_PATH="zh-cn/books/handbook"


for document in $(find "$NEW_PATH" -name "*.po" ); do

	echo $document
	name=$(basename "$document")
	python3 mc_translate.py --input $document --output $document --type chatgpt
	set +x
	git add zh-cn
    git commit -m "mc_translate_$name"
	git push
	set -x

done	
