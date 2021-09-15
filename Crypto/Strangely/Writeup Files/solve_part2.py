import zlib

list_of_crc = [0x3570E041, 0x654AB3A9, 0x5B22215B, 0x0E0D89E9, 0xD4F15C54, 0x6224C494, 0xB79C496B, 0x0DEB7416,
			   0xB1441D53, 0xA55CEB27, 0x05C3ACC9, 0x3DA99B67, 0x3F4D936A, 0x138AA87B, 0xA538E0A1, 0xB9DF8C6B,
			   0x01CE8D5D, 0x814B8BED, 0x717F3F79, 0x5C011BC9, 0xA48DBAA5, 0xE64AF817, 0xFCB6E20C]
temp = ['' for i in range(len(list_of_crc))]
s = ""
for i in range(32, 127):
    for j in range(32, 127):
        for k in range(32, 127):
            for l in range(32, 127):
                s += chr(i)
                s += chr(j)
                s += chr(k)
                s += chr(l)
                crc = zlib.crc32(s.encode())
                for x in range(len(list_of_crc)):
                    if (crc & 0xffffffff) == list_of_crc[x]:
                        print("File", x + 1, "contents: " + s)
                        temp[x] = s
                s = ""
res = ''.join(temp) + '}'
print(res)