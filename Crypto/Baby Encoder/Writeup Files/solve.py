from Crypto.Util.number import long_to_bytes
import numpy as np

encoded_flag = 28946494946812141829547706026065914605092406854105997612241563383442514740934913838546119691331952671988567947306226900850151388621540356510466883510328793101483278519506803779932615196763052658252298923048223762802716830885754352726914690907223838594044069643833511017514637891042919056
encoded_flag_str = (long_to_bytes(encoded_flag)).decode()


def displace(list, base):
    res = []
    for i in range(base):
        if (base + i >= len(list)):
            for j in range(base - 1, i - 1, -1):
                res.append(list[j])
            return res
        res.append(list[base + i])
        res.append(list[i])
    for j in range(len(list) - 1, 2 * base - 1, -1):
        res.append(list[j])
    return res


def flag_decoder():
    n = len(encoded_flag_str)
    test_list = [i for i in range(n)]
    for i in range(1, n):
        if (i % 6 == 0):
            test_list = displace(test_list, i)
    temp = [0 for i in range(n)]
    for i in range(n):
        temp[test_list[i]] = ord(encoded_flag_str[i])
    test_list = temp
    A = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    response = []
    for i in range(0, n, 3): 
        B = np.array(test_list[i : i + 3])
        X2 = np.linalg.solve(A,B)
        response.append(int(X2[0]))
        response.append(int(X2[1]))
        response.append(int(X2[2]))
    for i in range(n // 2):
        response[i] ^= response[n-i-1]
    response = response[::-1]
    flag = ['T', 'M', 'U', 'C', 'T', 'F', '{']
    for i in range(7, n):
        flag.append(chr((ord(flag[i-1]) ^ response[i])))
    flag = ''.join(flag)
    return flag


flag = flag_decoder()
print(flag)
