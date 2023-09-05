import sys

print("Here is the list infomation")
list=[1,2,3,4,5]
print(hex(sys.getrefcount(list)))
print(hex(sys.getsizeof(list)))
print(hex(id(list)))

print("\nHere is the tuple infomation")
tuple=("a","b","c","d","e")
print(hex(sys.getrefcount(tuple)))
print(hex(sys.getsizeof(tuple)))
print(hex(id(tuple)))

print("\nHere is the set infomation")
set={"a","b","c","d","e"}
print(hex(sys.getrefcount(set)))
print(hex(sys.getsizeof(set)))
print(hex(id(set)))

print("\nHere is the dict infomation")
dict={"a":1,"b":2,"c":3,"d":4,"e":5}
print(hex(sys.getrefcount(dict)))
print(hex(sys.getsizeof(dict)))
print(hex(id(dict)))
