#chake if number is neagtive or positive
import random
number = random.randint(-100, 105)
if number > 0:
    print(f"{number} is positive")
elif number ==0:
    print(f"{number} is zero")
else:
    print(f"{number} is neagtive")
