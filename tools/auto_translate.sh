NEW_PATH="zh-cn/books/handbook"


for document in $(find "$NEW_PATH" -name "*.po" ); do

	echo $document
	python3 tools/auto_translate.py --input $document --output $document

done	