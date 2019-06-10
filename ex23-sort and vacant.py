#DSA-Exer-23

def arrange_tickets(tickets_list):
    v=[0]*20
    for num in tickets_list:
        v.pop(int(num[1:])-1)
        v.insert(int(num[1:])-1,num)
    for x in range (len(v)):
        if v[x]==0:
            v[x]="V"
    first_ten = v[:10] 
    next_ten  = v[10:]
    while "V" in next_ten:
        next_ten.remove("V")
    for i in range (len(first_ten)):
        if first_ten[i] == "V":
            first_ten.pop(i)
            first_ten.insert(i,next_ten.pop(0))
    return first_ten
    #Remove pass and write your logic here
    pass

tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
