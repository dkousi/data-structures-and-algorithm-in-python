#DSA-Assgn-1

def merge_list(list1, list2):
    s = ''
    for x, y in zip(list1, list2[::-1]):
        if y and x:
            s += x + y
        elif x:
            s += x
        elif y:
            s += y
        s += ' '
    return s[:-1]

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
