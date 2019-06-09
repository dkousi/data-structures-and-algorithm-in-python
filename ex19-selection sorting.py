#DSA-Exer-19

def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    num_list[second_index],num_list[first_index]=num_list[first_index],num_list[second_index]


def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    return num_list.index(min(num_list[start_index:]))

def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    for i in range (len(num_list)):
        swap (num_list,i,find_next_min(num_list, i))


#Pass different values to the function and test your program
num_list=[13, 67, 23, 88, 10, 4, 55, 2]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)
