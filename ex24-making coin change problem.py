#DSA-Exer-24

def make_change(denomination_list, amount):
    denomination_list.sort(reverse=True)
    if amount == 0:
        return []
    else:
        for i in denomination_list:
            if amount%i==0:
                cha=amount//i
                break
            else:
                t=amount%i
                cha=amount//i
                for j in range (i+1,len(denomination_list)):
                    if t%denomination_list[j]==0:
                        cha=cha+(t//denomination_list[j])
                        if t==0:
                            break
        return cha
            
    '''Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    pass

#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
a=make_change(denomination_list, amount)
print(a)
