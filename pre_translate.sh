#!/bin/sh

ALL_COMPONENTS="Upstream/documentation"

NEW_PATH="zh-cn/books/handbook"

COMPONENTS="${1:-$ALL_COMPONENTS}"

GIT_IGNORE_FILES="toc-examples.adoc
toc-figures.adoc
toc-tables.adoc
toc.adoc
toc-1.adoc
toc-2.adoc
toc-3.adoc
toc-4.adoc
toc-5.adoc"

IGNORE_FILES="contrib-386bsd
contrib-additional
contrib-committers
contrib-corealumni
contrib-develalumni
contrib-portmgralumni"

for remove_file in $GIT_IGNORE_FILES; do
	find $ALL_COMPONENTS/content/en/ -name "$remove_file" -delete -print || exit 1
done

if [ ! -d " $NEW_PATH" ]; then
  mkdir -p $NEW_PATH
fi

rm -rf $NEW_PATH/*

for component in $COMPONENTS; do

	if [ ! -d "$component/content/en" ]; then
		echo "Directory '$component/content/en' not found."
		exit 1
	fi

	for document in $(find "$component/content/en/books/handbook" -name "*.adoc" ); do
		name=$(basename -s .adoc "$document")

		# Ignore some files
		if [ "$name" = "chapters-order" ]; then
			continue
		fi

		if [ "$document" = "documentation/content/en/books/books.adoc" ]; then
			continue
		fi

		if echo "$IGNORE_FILES" | grep -q -w "$name"; then
			continue
		fi

		dirbase=$(dirname "$document")

		# echo "$NEW_PATH/$(basename "$dirbase").po"
		python3 pre_translate.py --input $dirbase/$name.po --output $NEW_PATH/$(basename "$dirbase").po --tmx tmx.msg
		# cp "$dirbase/$name.po" "$NEW_PATH/$(basename "$dirbase").po"

		# po4a-updatepo \
		# 	--format asciidoc \
		# 	--option compat=asciidoctor \
		# 	--option tablecells=1 \
		# 	--option yfm_keys=title,part,description \
		# 	--master "$document" \
		# 	--master-charset "UTF-8" \
		# 	--copyright-holder "The FreeBSD Project" \
		# 	--package-name "FreeBSD Documentation" \
		# 	--po "$dirbase/$name.po"
		# if [ -f "$dirbase/$name.po~" ]; then
		# 	rm -f "$dirbase/$name.po~"
		# fi
	done
done
