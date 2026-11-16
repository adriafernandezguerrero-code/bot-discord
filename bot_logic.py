import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def gen_color():
    color = ["Rojo", "Azul", "Turquesa", "Amarillo", "Verde", "Rosa", "Morado"]
    return random.choice(color)

def gen_number():
    return random.randint(1,100)

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "CARA"
    else:
        return "SELLO"
