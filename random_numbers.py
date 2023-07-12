import random

def generate_random_numbers(num):
    numbers = []
    for _ in range(num):
        random_num = random.randint(1000000, 9999999)
        numbers.append(random_num)
    return numbers

random_numbers = generate_random_numbers(6)
print(random.choice(random_numbers))
