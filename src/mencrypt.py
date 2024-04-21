import numpy as np, string, random
from collections import Counter # is used to count occurrenc elementeve ne array ose lists

# numpy for array manipulation, string operation, random per random nr generation


print("MYSZKOWSKI TRANSPOSITION ENCRYPTION-DECRYPTION PROGRAM\n")
print("[MENU]")
print(" [1] Encrypt")
print(" [2] Decrypt")
number = 0
while number==0:
    select = input("Select menu: ")

    if select == "1":
        number=1
        text = input("\nEnter the text you want to encrypt: ")
        text = text.replace(" ", "")
        text = text.upper()
        key = input("Enter key: ")
        key = list(key.upper())
        sortkey = [] # empty list, store the key
        sortkey.append(key)
        sortkey.append([])
        i = 0
        while i<len(key):
            sortkey[1].append(i+1)
            i+=1
        sortkey = np.array(sortkey)
        newsortkey = sortkey [ :, sortkey[0].argsort()]
        sortkey = newsortkey.tolist()
        sortkey.append([])
        count = Counter(sortkey[0])
        i = 0
        n = 1
        while i<len(key):
            if count[sortkey[0][i]]>1:
                for j in range(count[sortkey[0][i]]):
                    sortkey[2].append(n)
                i+=(count[sortkey[0][i]]-1)
            else:
                sortkey[2].append(n)
            n+=1
            i+=1
        sortkey = np.array(sortkey)
        newsortkey = sortkey [ :, sortkey[1].argsort()]
        print("\n🔑:"+np.array2string(newsortkey[2],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        encrypt = []
        encrypt.append(key)
        for i in range (0, len(text), len(key)):
            x = text[i:i+len(key)]
            x = list(x)
            encrypt.append(x)
        while len(encrypt[len(encrypt)-1])<len(key):
            encrypt[len(encrypt)-1].append('X')
        encrypt = np.array(encrypt)
        print(" "+np.array2string(encrypt[1:len(encrypt)],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        newencrypt = encrypt [ :, encrypt[0].argsort()]
        count = Counter(newencrypt[0])
        result = []
        i = 0
        while i < len(newencrypt[0]):
            if count[newencrypt[0][i]] == 1:
                for j in range(1, len(newencrypt)):
                    result.append(newencrypt[j][i])
            else:
                for j in range(1, len(newencrypt)):
                    for k in range(i, count[newencrypt[0][i]] + i):
                        result.append(newencrypt[j][k])
                i += (count[newencrypt[0][i]] - 1)
            i += 1
        print("\nCiphertext =", end=' ')
        for i in range(len(result)):
            print(result[i], end='')
            if (i + 1) % (len(newencrypt) - 1) == 0:
                print(" ", end='')

    elif select == "2":
        number=2
        text = input("\nEnter the text you want to decrypt: ")
        text = text.replace(" ", "")
        text = list(text.upper())
        key = input("Enter key: ")
        key = list(key.upper())
        sortkey = []
        sortkey.append(key)
        sortkey.append([])
        i = 0
        while i<len(key):
            sortkey[1].append(i+1)
            i+=1
        sortkey = np.array(sortkey)
        newsortkey = sortkey [ :, sortkey[0].argsort()]
        sortkey = newsortkey.tolist()
        sortkey.append([])
        count = Counter(sortkey[0])
        i = 0
        n = 1
        while i<len(key):
            if count[sortkey[0][i]]>1:
                for j in range(count[sortkey[0][i]]):
                    sortkey[2].append(n)
                i+=(count[sortkey[0][i]]-1)
            else:
                sortkey[2].append(n)
            n+=1
            i+=1
        sortkey = np.array(sortkey)
        newsortkey = sortkey [ :, sortkey[1].argsort()]
        print("\n🔑:"+np.array2string(newsortkey[2],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        decrypt = []
        decrypt.append(key)
        decrypt.append([])
        i = 0
        while i<len(key):
            decrypt[1].append(i+1)
            i+=1
        decrypt = np.array(decrypt)
        newdecrypt = decrypt [ :, decrypt[0].argsort()]
        decrypt = newdecrypt.tolist()
        for i in range(int(len(text)/len(key))):
            decrypt.append([])
        count = Counter(decrypt[0])
        index = 0
        i = 0
        while i<len(key):
            if count[decrypt[0][i]]>1:
                for k in range(2,int((len(text)/len(key))+2)):
                    for j in range(count[decrypt[0][i]]):
                        decrypt[k].append(text[index])
                        index+=1
                i+=(count[decrypt[0][i]]-1)
            else:
                for k in range(2, int((len(text) / len(key)) + 2)):
                    decrypt[k].append(text[index])
                    index+=1
            i+=1
        decrypt = np.array(decrypt)
        result = decrypt [ :, decrypt[1].argsort()]
        print(" "+np.array2string(result[2:len(result)],formatter={'str_kind': lambda x: x},separator=' ')[1:-1])
        print("\nPlain Text =", end=' ')
        for i in range(2,len(result)):
            for j in range(len(result[0])):
                print(result[i][j], end='')
    else:
        print("[!] Please enter the appropriate options.")
