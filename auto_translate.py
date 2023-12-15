import polib
import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="机器翻译")
    parser.add_argument('--input', default=None,
                        dest='input', type=str, help='输入文件')
    parser.add_argument('--output', default=None,
                        dest='output', type=str, help='输出文件')
    args = parser.parse_args()
    po = polib.pofile(args.input)
    for i in po.fuzzy_entries():
        if 'delimited block . 4' not in i.comment:
            print(i.msgid)
            i.fuzzy = False
    po.save(args.output)