import polib
import argparse
import msgpack

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="机器翻译")
    parser.add_argument('--input', default=None,
                        dest='input', type=str, help='输入文件')
    parser.add_argument('--output', default=None,
                        dest='output', type=str, help='输出文件')
    parser.add_argument('--tmx', default=None,
                        dest='tmx', type=str, help='翻译类型')
    args = parser.parse_args()
    po = polib.pofile(args.input)
    tmx = msgpack.load(open(args.tmx,'rb'))

    for i in po.untranslated_entries():
        if 'delimited block . 4' not in i.comment:
            if i.msgid in tmx:
                    i.msgstr = tmx[i.msgid]
                    # i.fuzzy = False
    po.save(args.output)