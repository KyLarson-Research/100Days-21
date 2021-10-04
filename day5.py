#Author Kyle Larson 10-3-21
import random as r
l = input("How many letters would you like in your password?")
s = input("How many symbols would you like in your password?")
n = input("How many numbers would you like in your password?")

password =[]
for i in range(int(l)):
    case = r.randint(0,2)
    if case:
        password.append(chr(r.randint(97,123)))
    else:
        password.append(chr(r.randint(65,91)))
for i in range(int(s)):
    password.append(chr(r.randint(33,39)))
for i in range(int(n)):
    password.append(chr(r.randint(48,58)))
output = ""
r.shuffle(password)
output = output.join(password)
print(output)
