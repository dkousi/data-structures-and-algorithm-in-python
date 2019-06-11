#DSA-Tryout
import random
def generate_cards_per_type(card_type):
    card=[]
    s=""
    for i in range(2,11):
        s=card_type
        s+=str(i)
        card.append(s)
    temp=["J","Q","K","A"]
    for i in range(4):
        s=card_type
        s+=temp[i]
        card.append(s)
    return card
    
    #Remove pass and write your logic here
    pass

def generate_card_deck():
    cardlist=club+diamond+heart+spade
    return cardlist
    #Remove pass and write your logic here
    pass

def shuffle_card_deck(cards_list):
    random.shuffle(cards_list)
    return cards_list
    #Remove pass and write your logic here
    pass

def sort_cards_of_each_player(card_list):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    for x,y in card_list:
        sort_map = {c: i for i, c in enumerate(card_order)}
        sorted_candidates = sorted(y,
                           key=lambda card: (sort_map[card[0]], card[1]))
        cards_list[x]=sorted_candidates
    #Remove pass and write your logic here
    pass

def allocate_cards_to_players(cards_list):
    #Remove pass and write your logic here
    o,t,th,f=[],[],[],[]
    for i in range(14):
        o.append(cards_list[i])
        t.append(cards_list[i+1])
        th.append(cards_list[i+2])
        f.append(cards_list[i+3])
    carddic=dict()
    carddic["Player1"]=o
    carddic["Player2"]=t
    carddic["Player3"]=th
    carddic["Player4"]=f
    return carddic
    pass

def prepare_cards():
    global club
    club=generate_cards_per_type("C")
    global diamond
    diamond=generate_cards_per_type("D")
    global heart
    heart=generate_cards_per_type("H")
    global spade
    spade=generate_cards_per_type("S")
    cards_list=generate_card_deck()
    cards_list=shuffle_card_deck(cards_list)
    sortt=allocate_cards_to_players(cards_list)
    sortt=sort_cards_of_each_player(sortt)
    for x,y in sortt:
        if "CA" in y:
            return x
    #Remove pass and write your logic here
    

first_player=prepare_cards()
print("The first player is:",first_player)
