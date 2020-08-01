import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.shuffle([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))

# Generate Random Password
ASCII_LETTERS = string.ascii_letters
DIGITS = string.digits
print(''.join(random.choices(ASCII_LETTERS + DIGITS, k=8)))
