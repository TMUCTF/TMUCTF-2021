import pwn
from hashlib import sha1
from gmpy2 import xmpz, to_binary, invert, powmod, is_prime

rm = pwn.remote('185.235.41.166', 5000)
rm.recvlines(8)

for k in range(10):
	rm.recvlines(2)
	q = int(rm.recvline().strip().split()[2])
	rm.recvline()
	temp = rm.recvline().strip().split()
	msg1 = temp[0].decode().split("'")[1]
	s1 = int(temp[2])
	rm.recvline()
	temp = rm.recvline().strip().split()
	msg2 = temp[0].decode().split("'")[1]
	s2 = int(temp[2])
	rm.recvline()
	temp = rm.recvline().strip().split()
	s3 = int(temp[2])
	r = int(temp[3])
	rm.recvline()
	rm.recv()
	msg1 = str.encode(msg1, "ascii")
	msg2 = str.encode(msg2, "ascii")
	k = ((int(sha1(msg2).hexdigest(), 16) - int(sha1(msg1).hexdigest(), 16)) * invert(s2 - s1, q)) % q
	d = ((s1 * k - int(sha1(msg1).hexdigest(), 16)) * invert(r, q)) % q
	h = (s3 * k - d * r) % q
	rm.sendline(str(h))
	rm.recvline()
	secret = rm.recvline().strip().split()
	print(secret[5].decode(), "\n")

rm.close()
