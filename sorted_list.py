from sortedcontainers import SortedList, SortedKeyList

sorted_int_list = SortedList()
sorted_int_list.add(50)
sorted_int_list.add(20)
sorted_int_list.add(20)
sorted_int_list.add(10)
sorted_int_list.add(30) #binary search , are positions

print(sorted_int_list)
print(sorted_int_list.bisect_left(25)) #с левоЙ стороны ищет на какой позиции
print(sorted_int_list.bisect_right(30))
print(25 in sorted_int_list) # log

sorted_str_list = SortedList()
sorted_str_list.add("yazza")
sorted_str_list.add("hello")
sorted_str_list.add("aPPle")
sorted_str_list.add("banana")
sorted_str_list.add("Mango")
sorted_str_list.add("grape")
sorted_str_list.add("orange")
sorted_str_list.add("aPPle^")
sorted_str_list.add("^")

print(sorted_str_list)

sorted_key_list = SortedKeyList(key=str.casefold)
sorted_key_list.add("yazza")
sorted_key_list.add("hello")
sorted_key_list.add("aPPle")
sorted_key_list.add("banana")
sorted_key_list.add("Mango")
sorted_key_list.add("grape")
sorted_key_list.add("orange")
sorted_key_list.add("aPPle^")


print(sorted_key_list)







