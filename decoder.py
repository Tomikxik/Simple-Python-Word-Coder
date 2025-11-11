import random
coded = []
text = str(input("zadej slovo/a pro zasifrovani: ")).upper()
"""print(2*(len(text)//4) + (1 if len(text) % 4 != 0 else 0))"""     #matematic formule F1 :D

for j in range(3):
    temp = []
    for i in range(2*(len(text)//4) + (1 if len(text) % 4 != 0 else 0)):
        temp.append(chr(random.randint(65,90)))
    coded.append(temp)

characters = list(text)

"""print(f"{characters} <== word is here")"""
way = False                         #False => down , True => up
count = 1

position = 0
jump = 0

for j in range(len(text)):
    letter = characters[j]
    if (j - 3) % 4 == 0:
        if way:
            print(f"Short one placed here {coded[0][count]} {0,count} with this letter {letter} variation 1")
            coded[0][count] = letter
            way = False
            count += 2
            position += 1
        else:
            print(f"Short one placed here {coded[2][count]} {2,count} with this letter {letter} variation 2")
            coded[2][count] = letter
            way = True
            count += 2
            position -= 1
        jump += 2
    else:
        print(f"Long one placed here {coded[position][jump]} {position,jump} with this letter {letter}")
        coded[position][jump] = letter
        if way:
            position -= 1
        else:
            position += 1
        
def show(coded):
    for i in coded:
        print(*i)

print(text)
show(coded)