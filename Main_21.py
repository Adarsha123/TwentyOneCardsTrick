import random
import time
from cards import Cards

#print the dictionary

def dict_print(sets):
    tupled_set = zip(*[value for key, value in sets.items()])
    print(''.join(['Deck {:<20}'.format(key) for key in sets.keys()]))
    print()
    for row in tupled_set:
        print(''.join(['{:20}'.format(str(item)) for item in row]))



# knuth fisher yate shuffle


def shuffle(deck):

    for i in range(len(deck)-1,0,-1):
        j=random.randrange(i+1)
        if(i==j):
            continue
        deck[i],deck[j]=deck[j],deck[i]
    return deck


print("*****21 CARDS MAGIC*****")
print("GET READY!!")
print()
print("HERE IS YOUR DECK OF 21 CARDS(since it is 21 cards magic) ;) AND YOU HAVE FOLLOWING CARDS")
c = Cards()
full_deck = c.deck()
flag = "y"
shuffle(full_deck)
deck_21=full_deck[0:21]
print(*deck_21,sep='\n')
print()
print("KEEP ANY ONE OF THE CARDS IN YOUR MIND. I WILL READ YOUR MIND.....")
time.sleep(5)
round=["***First","***Second","***Third"]

for j in range(3):
    print(round[j]," Round***")
    print()
    sets = {0: [], 1: [], 2: []}
    for i in range(21):
        sets[i%3].append(deck_21[i])
    dict_print(sets)
    grp=int(input("    IN WHICH SET/DECK IS YOUR CARD ON???"))
    if(grp==0):
        a=random.randrange(1,3)
        deck_21=sets[a]+sets[0]+sets[3-a]
    elif(grp==2):
        a=random.randrange(2)
        deck_21=sets[a]+sets[2]+sets[2-a]
    else:
        deck_21=sets[0]+sets[1]+sets[2]
print("Okay! Lemme Guess <wink>")
time.sleep(3)
print("mmmm....")
time.sleep(2)
print("Your card is: ",deck_21[10])
print(" ;) ")



