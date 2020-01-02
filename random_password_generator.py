# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#passlen = 5

passlen=int(input("Enter the number between 5 and 15: "))

if passlen< 5:
    print("Enter the number between 5 and 15")
elif passlen>=5 and passlen<15:
    p =  "".join(random.sample(s,passlen))
    print (p)
else:
    print("Password length should not be greater than 15")
