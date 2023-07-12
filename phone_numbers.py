import random

def generate_random_numbers(num):
    numbers = []
    for _ in range(num):
        random_num = random.randint(10000000, 99999999)
        numbers.append(random_num)
    return numbers

random_number = generate_random_numbers(8)
print(random.choice(random_number))
