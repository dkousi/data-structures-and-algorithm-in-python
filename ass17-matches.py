#DSA-Assgn-17

def find_matches(country_name):
    #Remove pass and write your logic here
    l=[]
    for i in match_list:
        if (i[:3])==country_name:
            l.append(i)
    return l

def max_wins():
    #Remove pass and write your logic here
    cham,wor,t20,tmp,ret = [],[],[],[],dict()
    """ChampionShip Check"""
    for detail in match_list:
        split_detail = detail.split(":")
        if split_detail[1] == "CHAM":
            cham.append(split_detail[0])
            tmp.append(split_detail[3])
    if len(tmp) !=0:        
        while (min(tmp)!=max(tmp)):
            cham.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        ret ["CHAM"] = cham
    """T20 Check"""
    tmp = []
    for detail in match_list:
        split_detail = detail.split(":")
        if split_detail[1] == "T20":
            t20.append(split_detail[0])
            tmp.append(split_detail[3])
    if len(tmp) !=0:
        while (min(tmp)!=max(tmp)):
            t20.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        ret ["T20"] = t20

    """World Cup Check"""
    tmp = []
    for detail in match_list:
        split_detail = detail.split(":")
        if split_detail[1] == "WOR":
            wor.append(split_detail[0])
            tmp.append(split_detail[3])
    if len(tmp) !=0:
        while (min(tmp)!=max(tmp)):
            wor.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        ret ["WOR"] = wor 
    return ret
def find_winner(country1,country2):
    #Remove pass and write your logic here
    c1 = 0
    c2 = 0
    for d in match_list:
        split_d = d.split(":")
        #print (split_d[1])
        if split_d[0] == country1:
            c1+=int(split_d[3])
        elif split_d[0] == country2:
            c2+=int(split_d[3])
    if c1 > c2:
        return country1
    elif c2 > c1:
        return country2
    return "Tie" 

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print(find_matches("AUS"))
print(find_winner("IND", "AUS"))
print(max_wins())
