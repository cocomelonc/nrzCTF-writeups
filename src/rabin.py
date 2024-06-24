from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import inverse
from gmpy2 import mpz, iroot

# Given values
n = mpz(hex(6660423660188053350415327445344395338135348664790719040396624784336604853722943014761799620323706410444163431660904615208170337685693475970366287196615073))
c = mpz(hex(38080896768148850758642545706513383914345610328716157025260609118399922821551711687146033868308301448170383142388059914302445680656789037595253385481))

# Decryption
decrypted = iroot(c, 2)[0]

# Convert decrypted value to bytes and print as ASCII
flag = long_to_bytes(int(decrypted))
print(flag)