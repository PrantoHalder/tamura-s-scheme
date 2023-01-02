#tamura
import math
import random
#function defeinition
def prime(num):
    squreRoot = int(math.sqrt(num))
    for i in range(2, squreRoot+1):
        if num%i == 0:
            return False
    return True
def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1
    if (m == 1) :
        return 0
    while (a > 1) :
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0) :
        x = x + m0
    return x

#intilization phase
p = 170141183460469231731687303715884105727
q = 20988936657440586486151264256610222593863921
n = p * q
fiN = (p - 1) * (q - 1)
e = 0
for i in range(2, fiN):
    if prime(i) and fiN % i != 0:
        e = i
        break

d = modInverse(e, fiN)


print("---------  Initializing phase  ---------")
print("Public Keys(e,n):", e, n)
print("Private Keys(p,q,d):", p, q, d)

#encryption
m=788137579160089338861697153693
ciphertext=pow(m,e) % n
print("cipher text =",ciphertext)

#reencryption for authorith 2
p1 = 215621578848292125937382288471
q1 = 746592168710720377616088573229
n1 = p1 * q1
fiN1 = (p1 - 1) * (q1 - 1)
e1 = 0
for u in range(2, fiN1):
    if prime(u) and fiN1 % u != 0:
        e1 = u
        break

d1 = modInverse(e1, fiN1)


print("--------- reencryption phase for a2 ---------")
print("Public Keys(e,n):", e1, n1)
print("Private Keys(p,q,d):", p1, q1, d1)

ciphertext1=pow(ciphertext,e1) % n1
print("cipher text a1 =",ciphertext1)

#reencryption for authorith 2
p2 = 895848738169046499111615704593
q2 = 151667184419627348331511533307
n2 = p2 * q2
fiN2 = (p2 - 1) * (q2 - 1)
e2 = 0
for t in range(2, fiN2):
    if prime(t) and fiN2 % t != 0:
        e2 = t
        break

d2 = modInverse(e2, fiN2)


print("--------- reencryption phase for a1 ---------")
print("Public Keys(e,n):", e2, n2)
print("Private Keys(p,q,d):", p2, q2, d2)

ciphertext2=pow(ciphertext,e2) % n2
print("cipher text a2 =",ciphertext2)

#decryption
plaintext1=pow(ciphertext1,d)% n
print(plaintext1)
plaintext2=pow(ciphertext2,d)% n
print(plaintext2)
#redecryption
plaintext3=pow(plaintext1,d1) % n1
print(plaintext3)
plaintext4=pow(plaintext2,d2) % n2
print(plaintext4)

if(plaintext3/plaintext4==m):
    print("working")
else:
    print("it is not working")