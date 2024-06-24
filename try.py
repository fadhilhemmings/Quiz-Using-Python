import random 
for i in range(5):
    random.seed(3) # anda dapat menganti angka 0 dengan angka berapapun
    print(random.randint(1, 1000))