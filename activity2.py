my = {}
my = {"Name" : "Bhavi", "Age" : 14 }
print(my)
int1 = {}
int1 = {1 : "One", 2 : "Two", 3 : "Three"}
print(int1)
mix = {"Place" : "KL" , 5 : "Number"}
print(mix)
name = {"Name" : "Bhavi", 1 : [2,4,6,8]  }
print(name)
print(my["Name"], "the value of Name is")
print(int1.get(2), "is the value of key 2")
mix["Place"] = "Johor"
print(mix)
mix.pop(5)
print(mix)
my.clear()
print(my)
int1.clear()
print(int1)
mix.clear()
print(mix)
name.clear()
print(name)
