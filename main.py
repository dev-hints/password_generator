import random
lw = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
sym = "@3$&*?/"
comb = lw + up + num + sym
length = 8
password = "".join(random.sample(comb, length))
print(password)
