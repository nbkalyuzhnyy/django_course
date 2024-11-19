import random

def random_word():
    ret = u''
    words = ["компьютер", "ноутбук", "монитор", "клавиатура"]
    ret += random.choice(words)
    return ret, ret 
