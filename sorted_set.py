from sortedcontainers import SortedSet

sorted_str_set = SortedSet()
sorted_str_set.add("hello")
sorted_str_set.add("World")
sorted_str_set.add("hello")
sorted_str_set.add("world")
sorted_str_set.add("hello")
sorted_str_set.add("world")

print(sorted_str_set)