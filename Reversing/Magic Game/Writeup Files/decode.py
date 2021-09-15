import binascii

def decode(string,initial):
    alph = "abcdefghijklmnopqrstuvwxyz"
    rot = initial
    decoded = ""
    for i in range(len(string)):
        c = string[i]
        plain = alph[(alph.index(c) + rot) % (len(alph) - 1)]
        decoded += plain
        rot += ord(plain) - 2
    return decoded  


def find_decoding(num):
    a = num
    num = rev(num)
    num = format(num, 'x')
    num = binascii.unhexlify(num)
    num = num.decode()
    for i in range(26):
        decoded = decode(num,i)
        if ((ord(decoded[-1]) + 5) % 25) == i:
            print("magic input equal with %d is:  %s" % (a, decode(num,i)))


def rev(num):
    a = str(num)[::-1]
    return int(a)


ops= [4932739181, 6122352081, 3611099681, 5122107891, 3550866391, 3983866391, 8920866391, 6610774871]
for op in ops:
    find_decoding(op)

