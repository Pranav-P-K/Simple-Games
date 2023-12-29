import random
from words import word_list

def comp_word():
    cw = random.choice(word_list)
    if len(cw) < 5 or len(cw) > 11:
        comp_word()
    else:
        #print(cw)
        game(cw.upper())

def game(w):
    trys = (len(w))*2
    uwl = list("-"*len(w))
    for chance in range(trys):
        uw = input("\nEnter a character (A-Z):").upper()
        for i in range(len(w)):
            if w[i] == uw:
                uwl[i] = w[i]
        for j in uwl:
            print(j,end="")
        if uwl == list(w):
            print("\nYOU ARE WINNER!\nGAME OVER!!")
            break
    print("\n",w)
    
if __name__ == "__main__":
    comp_word()