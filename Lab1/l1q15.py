import time
import string
import random

# lowercase
# uppercase
# numbers
# symbol

# printable - contains letter(uppercase&lowercase) + digits + punctuation


def get_random_password(pass_len):
    pass_char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(pass_char)
                       for i in range(pass_len))
    return password


Starttime = time.time()
pass_len = random.randint(10, 20)
print("Password length : " + str(pass_len))
print("Password : " + get_random_password(pass_len))
Endtime = time.time()
print("Time taken (s): " + str((Endtime - Starttime)*1000))
