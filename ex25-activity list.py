#DSA-Exer-25
def find_maximum_activities(activity_list,start_time_list, finish_time_list):
    A = [activity_list[0]]
    k = 0

    for i in range(1,len(activity_list)):
        if start_time_list[i] >= finish_time_list[k]:
            A.append(activity_list[i])
            k=i
    return A        
#Pass different values to the function and test your program
activity_list=[1,2,3,4,5,6,7]
start_time_list=[1,4,2,3,6,8,6]
finish_time_list=[2,6,4,5,7,10,9]

print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)
