# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Writeup
Reviewing the code of this challenge, we find that a message is encrypted using the AES-CBC algorithm. Flag is the IV used to encrypt the first block and the key (except 3 bytes) is given.
Some bytes of the encrypted message is also given in the output file.

Since the last 21 bytes of the encrypted message are given (16 bytes for the last block and 5 bytes for the one before the last), the last block can be decrypted.
As we know, in the AES-CBC algorithm, the IV used to decrypt the last block is equal to the encrypted value of the previous block.
Since we only have 5 bytes of the block before the last, we set the first 11 bytes of the IV equal to zero.
In this way, we decode the last block using all possible values of the key, and by comparing the last 5 bytes of the decrypted value with the last 5 bytes of the clear text message, we obtain the key.
It should be noted that the last 5 bytes of the clear text message are equal to "\n\n\n\n\n" (to understand this, refer to the `pad` function).

After obtaining the key, we decrypt the last block using the obtained key. To do this, we set the IV to zero. Therefore, we obtain the encrypted value of the block before the last (which is also the IV used to encrypt the last block) by XORing the decrypted result with the last block of the clear text message.
By repeating this for the previous blocks, we finally get the flag, which is the IV of the first block. The solution code for this challenge is as follows (also available in [solve.py](https://github.com/TMUCTF/TMUCTF-2021/blob/main/Crypto/435!/Writeup%20Files/solve.py)):
```python
from Crypto.Cipher import AES
import binascii, sys
import hashlib
import string
from crypto_commons.generic import xor_string,xor
import string

key = b'*XhN2*8d%8Slp3*v'
key_len = len(key)


def pad(message):
    p = bytes((key_len - len(message) % key_len) * chr(key_len - len(message) % key_len),encoding='utf-8')
    return message + p

	
def encrypt(message,passphrase,iv):
    aes = AES.new(passphrase, AES.MODE_CBC, iv)
    return aes.encrypt(message)

	
def decrypt(message, passphrase, iv):
    aes = AES.new(passphrase, AES.MODE_CBC, iv)
    return aes.decrypt(message)

	
def find_key():
    key = '{}XhN2{}8d%8Slp3{}v'
    for c1 in string.printable:
        for c2 in string.printable:
            for c3 in string.printable:
                temp = decrypt(binascii.unhexlify('1f3ef3fab2bbfc838b9ef71867c3bcbb'), key.format(c1, c2, c3).encode('utf8'), binascii.unhexlify('0' * 22 + '9f43fd6634'))
                if temp[-5:] == b'\n\n\n\n\n':
                    return key.format(c1, c2, c3).encode('utf8')

					
def find_block(encrypted_block, message_block):
    c1 = decrypt(binascii.unhexlify(encrypted_block), key, binascii.unhexlify(b'0' * 32))
    result = b''
    for i in range(16):
        result += bytes([c1[i] ^ message_block[i]])
    return binascii.hexlify(result)



key = find_key()
					
print("Key:", key.decode('utf8'))

h = hashlib.sha256(key).hexdigest()
hidden_message = binascii.unhexlify(h)[:10]
message = b'CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption' + hidden_message
complete_message = pad(message)
complete_message = [complete_message[i:i+16] for i in range(0, len(complete_message), 16)]

encrypted = '9**********b4381646*****01********************8b9***0485******************************0**ab3a*cc5e**********18a********5383e7f**************1b3*******9f43fd66341f3ef3fab2bbfc838b9ef71867c3bcbb'.replace('*', '0')
encrypted = [encrypted[i:i+32] for i in range(0, len(encrypted), 32)]

for i in range(1, len(encrypted) + 1):
    temp = find_block(encrypted[-i], complete_message[-i])
    if i == len(encrypted):
        flag = binascii.unhexlify(temp)
    else:
        encrypted[-i-1] = temp

print("Flag:", "TMUCTF{" + flag.decode('utf8') + "}")
```
The flag:
```
TMUCTF{Y0U_D3CrYP73D_17}
```
