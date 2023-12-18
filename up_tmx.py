import polib
import argparse
import msgpack

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="机器翻译")
    parser.add_argument('--input', default=None,
                        dest='input', type=str, help='输入文件')
    parser.add_argument('--tmx', default=None,
                        dest='tmx', type=str, help='tmx文件')
    args = parser.parse_args()
    try:
        tmx = msgpack.load(open(args.tmx,'rb'))
    except Exception as e:
        tmx = {}
    po = polib.pofile(args.input)
    for i in po.translated_entries():
        tmx[i.msgid] = i.msgstr
    
    msgpack.dump(tmx,open(args.tmx,'wb'))
