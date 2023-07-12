import random

kikuyu_names = ["Wanjiru", "Mwangi", "Njeri", "Kamau", "Wambui", "Njoroge", "Waweru", "Muthoni", "Mwangi", "Nyambura"]
kamba_names = ["Mutisya", "Mwende", "Musyoka", "Kioko", "Mbithe", "Muthoka", "Mutua", "Mwikali", "Nthenya", "Kavata"]
luo_names = ["Odhiambo", "Akinyi", "Omondi", "Atieno", "Ochieng", "Achieng", "Owuor", "Adhiambo", "Oyoo", "Otieno"]
luhya_names = ["Wangila", "Nekesa", "Were", "Wanjala", "Wamalwa", "Namachanja", "Shikuku", "Nandwa", "Mukhisa", "Mmbadi"]
swahili_names = ["Juma", "Amina", "Said", "Zainabu", "Ali", "Fatuma", "Salim", "Halima", "Mwanaidi", "Hassan"]

all_names = []
all_names.extend(kikuyu_names)
all_names.extend(kamba_names)
all_names.extend(luo_names)
all_names.extend(luhya_names)
all_names.extend(swahili_names)

random_last_name = random.choice(all_names)
