NEW_PATH="zh-cn/books/handbook"


for document in $(find "$NEW_PATH" -name "*.po" ); do

	echo $document
	python3 tools/up_tmx.py --input $document --tmx tools/tmx.msg

done	