my_list = [0, 5]
print(my_list[0])
print(my_list[1])
print(len(my_list))
my_list.append(10)# why my_list2 is not defined
print(len(my_list))
my_list.remove(0)
print(f"first no.0: {my_list[0]}, length: {len(my_list)}")
my_list.sort()
print(my_list[1])
print(my_list.index(5))
my_list[0] = 55
print(f"second no.0: {my_list[0]}")


#正确写法
my_list.append(10)
my_list2 = my_list
print(my_list2)                # 输出 [0, 5, 10]
#注意：Python中对原列表操作的方法一般都返回None。


#dict
my_dict = {"west": 1, "east": 2, "south": 3, "north": 4}
    #dict add
my_dict["spurs"] = 123
print(my_dict)
    #dict look up
print(my_dict['north'])
    #dict remove
del my_dict['east']
print(f"after remove east: {my_dict}")
my_dict["north"]=4444  # 0004 IS NO T ALLOW
print(f"change north number: {my_dict['north']}")


#在Python中，数字前加0被认为是**八进制数（octal）**的表示方法，且不能包含8，或9.
#如果一定要用前导0表示，则必须作为字符串：
#my_dict["north"] = "0004"


#TUPLE
my_tuple = (1, 2, 3, 4, 5)


    #tuple add how???
print(my_tuple)
print(my_tuple[0], my_tuple[4])  #1 5


#元组（tuple）是不可变的，一旦创建，就无法修改。

#如果想『添加』元素，必须通过创建新tuple
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4,)   # 注意 (4,) 是一个元素的元组
print(my_tuple)              # 输出 (1, 2, 3, 4)

#set
my_set = set('hello')  #如何添加hello完整的，print是hello
print(len(my_set))
print("i" in my_set)
print(my_set)
my_set.add("w o r l d")
print(my_set)
#添加完整字符串
my_set = set()          # 初始化为空set
my_set.add('hello')     # 完整字符串
print(my_set)           # {'hello'}