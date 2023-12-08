import random

password_len = int(input("Enter the length of password: ")) 
letters = "abcdefghijklmnopqrstuvwxyz"
letters = [l for l in letters]

num = "1234567890"
num = [n for n in num]

symbol = "@#$%&!?"
symbol = [s for s in symbol]

password = []
all_char = letters+num+symbol

random.shuffle(all_char)
random.shuffle(all_char)

for x in range(password_len):
    temp = random.choice(all_char)
    password.append(temp)
password = "".join(password)
print(password)