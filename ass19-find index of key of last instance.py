#DSA-Assgn-19

def last_instance( num_list,  start,  end,  key):
    #Remove pass and write your logic here
    c,err=0,0
    for i in num_list[::-1]:
        if i==key:
            c+=1
        else:
            err=1
    if c==0:
        return -1
    return num_list.index(key)+c-1

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")
