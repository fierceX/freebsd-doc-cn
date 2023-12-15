NEW_PATH="zh-cn/books/handbook"


for document in $NEW_PATH/*; do

	echo $document
	python3 auto_translate.py --input $document --output $document
    set

done	