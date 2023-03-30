import random
  
with open("./czech-words.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

print(random.choice(slova))
