#DSA-Tryout
import random
def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
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
              return mid,guesses
#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    r=random.randrange(1,n)
    (f,guess)=find_it(r,list_of_elements)
    print("success and number of guesses=",guess)
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.

#Pass different values to play() and observe the output
play(400)
