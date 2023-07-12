import random

male_names = ["James", "John", "Joseph", "David", "Peter", "Samuel", "Paul", "Daniel", "Michael", "Mark", "Robert", "Charles", "Simon", "Thomas", "Andrew", "Patrick", "Stephen", "Kevin", "Joshua", "Brian", "Collins", "Brian", "George", "Eric", "Henry", "Francis", "Moses", "Kennedy", "Vincent", "Samson", "Nicholas"]
female_names = ["Mary", "Grace", "Elizabeth", "Sarah", "Catherine", "Joyce", "Mercy", "Esther", "Alice", "Rose", "Lilian", "Sophia", "Monica", "Caroline", "Priscilla", "Dorothy", "Faith", "Ruth", "Angela", "Beatrice", "Wangari", "Evelyn", "Julia", "Nancy", "Gladys", "Hannah", "Susan", "Janet", "Mabel", "Purity"]

kenyan_first_names = []
kenyan_first_names.extend(male_names)
kenyan_first_names.extend(female_names)

random_names = random.choice(kenyan_first_names)
print(random_names)
