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
            try:
                if len(i.msgstr) > 1:
                    if i.msgid[-1] == '\n' and i.msgstr[-1] != '\n':
                        i.msgstr += '\n'
                    if i.msgstr[-1] == '\n' and i.msgid[-1] != '\n':
                        i.msgstr = i.msgstr.rstrip('\n')
                    i.fuzzy = False
            except Exception as e:
                print(e)
                print(i.msgid,args.input)
    po.save(args.output)