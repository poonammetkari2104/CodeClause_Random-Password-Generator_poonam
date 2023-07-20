import random


def generatePassword(m):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()"
    password = ""
    for i in range(m):
        password = random.choice(characters)+password
    return password

n = 10
password = generatePassword(n)
print("randomly generate password is:", password)
