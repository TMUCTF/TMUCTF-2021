def eight(dis):
    a = int(dis / 8)
    b = int(a / 122)
    c = a % 122
    if chr(c).isalnum():
        return b, c, 0
    else:
        b=int(a / 122) - 1
        c= a - b * 122
        if chr(c).isalnum():
            return b, c, 0
        elif c % 2 == 0:
            if chr(int(c / 2)).isalnum():
                return b, int(c / 2), int(c / 2)
            else:
                return b, 100, c - 100
        else:
            if chr(int(c / 2)).isalnum():
                return b, int(c / 2), int(c / 2) + 1 
            else:
                return b, 100, c - 100


def multiples(count):
    global magicinputs
    for i in range(int(count / 8), 0, -1):
        a = count - i * 8
        if a % 3 == 0:
             if chr(int(a / 3)).isalnum():
                return chr(int(a / 3))


def swch():
    global num1, num2, magicinputs
    a = num1
    num1 = num2
    num2 = a
    magicinputs.append("1swch")


num1 =  int(input("num1: "))
num2 = int(input("num2: "))
magicinputs = []
dis = num1 - num2
if dis < 0:
    swch()
a = multiples(num1 - num2)
magicinputs.append(a + "upth")
for i in range(0, ord(a)):
    num1 -= 2
    num2 += 1
swch()
b, c, d = eight(abs(num1 - num2))
magicinputs.append(chr(c) + "dwei")
if d != 0:
    magicinputs.append(chr(d) + "dwei")
for i in range(0, b):
    magicinputs.append("zdwei")
print(magicinputs)    