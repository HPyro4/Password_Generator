import string
import random

def generator():
    str1 = string.ascii_uppercase
    str2 = string.ascii_lowercase
    str3 = string.digits
    str4 = string.punctuation

    passlen = int(input('Please enter password length \n: '))

    lst = []
    lst.extend(list(str1))
    lst.extend(list(str2))
    lst.extend(list(str3))
    lst.extend(list(str4))

    random.shuffle(lst)
    print("".join(lst[0:passlen]))


generator()
