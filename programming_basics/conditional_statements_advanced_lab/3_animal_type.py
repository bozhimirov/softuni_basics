animal = input()
# dog mammal
# snake crocodile tortoise reptile
#other unknown
if animal == "dog":
    print('mammal')
elif animal == "snake" or animal == "crocodile" or animal == "tortoise":
    print("reptile")
else:
    print("unknown")
