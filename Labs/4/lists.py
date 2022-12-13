# Task 1: Accessing a Value

dev_tools = ['JavaScript', 'Python', 'Java', 'Django', 'React']
print(dev_tools[1])



# Task 2: Adding and Changing Values

instructors = ['Nevin', 'Mike', 'Jake', 'Dan', 'Megan']
instructors += ['Dan', 'James', 'John-Boy']
instructors[5] = 'Danimal'
print(instructors)



# Task 3: Popping a Value

instructors.pop()
print(instructors)



# Task 4: Removing a Value

instructors.pop(1)
print(instructors)



# Task 5: Looping over a List

l1 = ['fan', 'bull-', 'high-', 'barrel-o-', 'slap']
l2 = ['dango', 'rider', 'horse', 'monkeys', 'stick']

for i in range(len(l1)):
    print(l1[i] + l2[i])



# Task 6: List Function

first_names = ['Carl', 'Jimmy', 'Sheen', 'Cindy']
name = 'Goddard'
duplicates = False

for i in first_names:
    if i == name:
        duplicates = True

if duplicates == False:
    first_names.insert(-1, name)

print(first_names)



# Task 7: Joining Lists

fav_destinations = ['Grand Canyon', 'San Francisco']
travel_destinations = ['San Antonio', 'Lisbon', 'Chicago']

# 1
one = fav_destinations + travel_destinations
print(one)

# 2
for i in travel_destinations:
    fav_destinations.append(i)
print(fav_destinations)

# 3
three = []
three.extend(fav_destinations)
three.extend(travel_destinations)
print(three)

# List Comprehension
list_comp = [des for des in fav_destinations + travel_destinations]
print(list_comp)



# Task 8: Copy Lists

vehicles = ['Ripstick', 'Jetpack', 'Plane']

copy1 = []
for v in vehicles:
    copy1.append(v)
print(copy1)

copy2 = vehicles.copy()
print(copy2)

copy3 = list(vehicles)
print(copy3)

copy4 = [v for v in vehicles]
print(copy4)



# Task 9: Sort Lists

fav_dishes = ['Chicken Burrito', 'General Tso Chicken Rice Bowl', 'Nashville Hot Chicken', 'Spaghetti with Vodka Sauce', 'Margherita Pizza']

# Ascending
fav_dishes.sort()
print(fav_dishes)

# Descending
fav_dishes.sort(reverse=True)
print(fav_dishes)

# Ascending
print(sorted(fav_dishes))

# Descending
print(sorted(fav_dishes, reverse=True))


