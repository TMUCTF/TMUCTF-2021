def decrypt():
    with open('file', 'rb') as f:
        rar_header = [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x00]
        data = f.read()
        key = [int(data[i]) ^ rar_header[i] for i in range(7)]
        with open('result.rar', 'wb') as f:
            for i in range(len(data)):
                f.write(chr(int(data[i]) ^ key[i % 7]).encode('ISO-8859-1'))


decrypt()
