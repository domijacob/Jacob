#SECTION 1
#The End Goal
market = ["Yam","Tomato","Onion"]
print(market)
market.append("Fish")
print(market)

# #Precise Entry
grades = ["80","90","70"]
print(grades)
grades.insert(1,85)
print(grades)

# #The Clean Up
gadgets = ["Laptop","Phone","Tablet","Phone"]
print(gadgets)
gadgets.remove("Phone")
print(gadgets)

# #Wipe Out
colors = ["Red","Blue","Green"]
print(colors)
del colors
print(colors)

# #Frequency Check
votes = ["Yes","No","Yes","Yes","No"]
print(votes)
print(votes.count("Yes"))

#The Slice
alphabets = ["a","b","c","d","e","f"]
print(alphabets)
print(alphabets[2:5])

#Flip It
students = ["Kofi","Ama","Yaw"]
students.reverse()
print(students)

#Merging
list_a = [1,2]
list_b = [3,4]
list_a.extend(list_b)
print(list_a)

#The Pop
cities = ["Accra","Kumasi","Tamale"]
print(cities)
removed_cities = cities.pop(2)
print(removed_cities)

#The Search
items = ["Pen","Ruler","Eraser"]
print(items)
items.index("Ruler")
print(items.index)

#SECTION 2
#The Tuple Wall
student_info = ("Araba",20)
print(student_info)
student_info[1] = 21
#Error says-TypeError: 'tuple' object does not support item assignment

#The Switch
tup = (1,2,3)
tup_change = list(tup)
print(tup_change)
tup_change.append(4)
print(tup_change)
tup = tuple(tup_change)

#Count the Items
data = (10,20,10,30,10)
print(data)
data.count(10)
print(data.count())

#Positon Finder
colors = ("Red", "Blue", "Green")
print(colors.index("Blue"))

#Unpacking
coords = (5.6, -0.1)
lat= coords[0]
lon= coords[1]
print(lat)
print(lon)

#Nesting
nest = []
nest.append((5, 10))
print(len(nest))

#Tuple Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[-2:])

#Mixed Extend
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)

#Memory Wipe
my_tup = (1, 2, 3)
del my_tup

#Type Check
x = (5)
y = (5,)
print(type(x))
print(type(y))