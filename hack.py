import random

password = random.randint(1, 10000000)

key = 0
n = 0
print("Взлом пароля...")

while n < password:
    if password == key:
        break
    else:
        key += 1
        n += 1

print("Ура! Пароль взломан! Пароль => ", key)