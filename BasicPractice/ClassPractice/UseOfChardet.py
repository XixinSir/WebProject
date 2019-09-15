import chardet

UTF8_TEXT="你好，世界".encode('utf-8')
SJIS_TEXT="哈哈哈".encode('GB2312')
GBK_TEXT="中国加油！".encode('GBK')

def main():
    print(chardet.detect(UTF8_TEXT))
    print(chardet.detect(SJIS_TEXT))
    print(chardet.detect(GBK_TEXT))

if __name__ == '__main__':
    main()
