from sortedcontainers import SortedDict


sorted_dict = SortedDict()
sorted_dict['c']=30
sorted_dict['a']=10
sorted_dict['b']=20

print(sorted_dict)
print(sorted_dict.peekitem(0))
print(sorted_dict.peekitem(-1))