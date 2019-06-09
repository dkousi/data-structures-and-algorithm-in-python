#DSA-Tryout

import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #remove pass and copy the code written earlier for linear search
    guess=0
    for i in element_list:
        if i==num:
            return guess
        else:
            guess+=1

def find_it_binary(num,element_list):
    #remove pass and copy the code written earlier for binary search
    guesses=0
    low=element_list[0]
    high=element_list[len(element_list)-1]
    while (low <= high):
          mid = (low + high) // 2
          if (element_list[mid] > num):
              high = mid - 1
              guesses+=1
          elif (element_list[mid] < num):
              low = mid + 1
              guesses+=1
          else:
              return guesses

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    rand_index=random.randrange(0,len(list_of_elements))
    rand_num=list_of_elements[rand_index]
    print("Number to be guessed:",rand_num)
    start=timer()
    print("No. of guesses made using linear search:",find_it_linear(rand_num,list_of_elements))
    end=timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format( (end-start)))
    start=timer()
    print("No. of guesses made using binary search:",find_it_binary(rand_num,list_of_elements))
    end=timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format( (end-start)))

#Pass different values to play() and observe the output
play(40000)
