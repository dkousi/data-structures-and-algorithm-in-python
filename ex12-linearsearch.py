#DSA-Tryout

import random

def find_it(num,element_list):
    for i in element_list:
        if i==num:
            return True
        break
    return False
    #Remove pass and copy the solution earlier written for this function here
    #Modify it, if required

def initialize_list_of_elements(n):
    #Modify the code to initialize the list of elements in ascending order
    #Try with descending order also
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    '''mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1'''
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    r=random.randrange(1,n)
    f=find_it(r,list_of_elements)
    if f:
        print("success")
    else:
        print("fail")
    #Remove pass and copy the solution earlier written for this function here


#Pass different values to play() and observe the output
play(4)
