my_list = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]#如何使用切片创造
my_list.append(20)
print(len(my_list))
print(my_list)
my_list.remove(5)
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
#my_list[1:5]
print(my_list[1:5])


#dict
my_dict = {"apple": 5, "banana": 3, "orange": 4}
print(my_dict)
my_dict["grape"]=10
print(my_dict)
del my_dict["banana"]
print(my_dict)
my_dict["apple"]=2*5
print(my_dict)

#tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
my_tuple = my_tuple + (6, 7, 8)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1:4])

#set
my_set = set()
my_set.add("hello")
my_set.add("world")
print(my_set)
my_set.remove("world")
print(my_set)
print("hello" in my_set)

