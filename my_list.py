my_list=[]
print(my_list)
#Adding elements to the list using append
my_list.append(10)
print(my_list)  # Display the list after adding element 10
my_list.append(20)
print(my_list)  # Display the list after adding element 20
my_list.append(30)
print(my_list)  # Display the list after adding element 30
my_list.append(40)
print(my_list)  # Display the list after adding element 40
my_list.insert(1, 15)  # Insert 15 at the second position
print(my_list)  # Display the list after inserting element 15
my_list.extend([50,60,70])  # Extend the list with multiple elements    
print(my_list)  # Display the list after extending with [50, 60, 70]
my_list.pop()  # Remove the last element 70 from the list
print(my_list)  # Display the list after removing element 70
my_list.sort()  # Sort the list in ascending order
print(my_list)  # Display the list after sorting
#Find and print the index of the value 30 in my_list.
print(my_list.index(30))  # Display the index of the value 30