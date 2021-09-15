# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Writeup
In this challenge we have only an encrypted file without any other information. One of the first cryptographic methods that comes to mind in such cases is the classic XOR cryptography.
One common way to find the key of XOR cryptography is to XOR the first few bytes of the file with the header of common file types and use the result as a key. 
If we get a valid file by XORing the obtained key with all the bytes of the file, we will realize that the key is correct.
In this challenge, if we use the RAR file header as mentioned, we will finally get a valid RAR file. 
The solution code for the this part of the challenge is as follows (also available in [solve_part1.py](https://github.com/TMUCTF/TMUCTF-2021/blob/main/Crypto/Strangely/Writeup%20Files/solve_part1.py)):
```python
def decrypt():
    with open('file', 'rb') as f:
        rar_header = [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x00]
        data = f.read()
        key = [int(data[i]) ^ rar_header[i] for i in range(7)]
        with open('result.rar', 'wb') as f:
            for i in range(len(data)):
                f.write(chr(int(data[i]) ^ key[i % 7]).encode('ISO-8859-1'))


decrypt()
```  
The obtained RAR file is [result.rar](https://github.com/TMUCTF/TMUCTF-2021/blob/main/Crypto/Strangely/Writeup%20Files/result.rar). 
This file has a password, and it is not possible to obtain the password using common password-breaking algorithms (brute-force or dictionary attacks). 
With a little attention to the contents of the RAR file, we find that it contains 23 small files (maximum 4 bytes). 
So we can get their contents by obtaining CRC code from all 4-byte strings and comparing the result with the CRC codes of the files. 
The solution code for the second part of the challenge is as follows (also available in [solve_part2.py](https://github.com/TMUCTF/TMUCTF-2021/blob/main/Crypto/Strangely/Writeup%20Files/solve_part2.py)):
```python
import zlib

list_of_crc = [0x3570E041, 0x654AB3A9, 0x5B22215B, 0x0E0D89E9, 0xD4F15C54, 0x6224C494, 0xB79C496B, 0x0DEB7416, 0xB1441D53, 0xA55CEB27, 0x05C3ACC9, 0x3DA99B67, 0x3F4D936A, 0x138AA87B, 0xA538E0A1, 0xB9DF8C6B, 0x01CE8D5D, 0x814B8BED, 0x717F3F79, 0x5C011BC9, 0xA48DBAA5, 0xE64AF817, 0xFCB6E20C]
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
```  
The output of this program that shows the contents of each file is as follows:
```
File 14 contents:	!_Y0
File 9 contents:	3_f0
File 19 contents:	4lcu
File 17 contents:	4v3_
File 16 contents:	57_h
File 22 contents:	5_:)
File 18 contents:	70_c
File 11 contents:	7h3_
File 12 contents:	P455
File 2 contents:	TF{7
File 1 contents:	TMUC
File 13 contents:	W0rD
File 7 contents:	_70_
File 21 contents:	_cRc
File 5 contents:	_n0_
File 4 contents:	_w45
File 8 contents:	bru7
File 3 contents:	h3r3
File 20 contents:	l473
File 6 contents:	n33d
File 10 contents:	rc3_
File 15 contents:	u_ju
```  
The flag:
```
TMUCTF{7h3r3_w45_n0_n33d_70_bru73_f0rc3_7h3_P455W0rD!_Y0u_ju57_h4v3_70_c4lcul473_cRc5_:)}
```
