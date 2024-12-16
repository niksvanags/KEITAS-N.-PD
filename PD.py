#2 uzdevums
n = int (input ("ievadi skaitli:"))
summa = 0
for i in range (1,1 + n):
    summa = i
    print  ("skaitļu summa no 1 līdz n ir:",summa)

#3 uzdevums
n = int (input ("ievadi skaitli:"))
faktorials = 1
for i in range (1,1 + n):
    faktorials *= i
    print ("skaitļu faktorials no 1 līdz n ir:", faktorials)

#4 uzdevums
n = int (input ("ievadi skaitli:"))
for i in range (n, -1, -1):
    print (1)
    
#5 uzdevums
lenght = int (input ("lenght:"))
for i in range (lenght, 0, -1):
    print ("*" * i)
    
#6 uzdevums
import random
min_skaitlis = 1
max_skaitlis = 100
iedomata_skaitlis = random.randint (min_skaitlis, max_skaitlis)
print (f"ludzu uzminet skaitli intervala no {min_skaitlis}")
minesanas_reizes =0
while True:
    lietotaja_ievade = int (input ("ievadi savu minejumu:"))
    minesanas_reizes = 1
    if lietotaja_ievade < iedomata_skaitlis:
        print ("lielaks!")
    elif lietotaja_ievade < iedomata_skaitlis:
        print ("mazaks!")
    else:
        print (f"uzminets! skaitlis ir {iedomata_skaitlis}.")
        break
print(f"skaitijat minesanu {minesanas_reizes} reizes.")