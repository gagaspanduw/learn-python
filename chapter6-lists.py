fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print (fruits, years)

# to check membership in a lists
print("apple" in fruits) # result False
print("apples" in fruits) # result True

# to check how many value in a lists
print(fruits.count("apples")) #result 1
print(fruits.count("apple")) #result 0

# to check position the result is the first value
# if there is more than 1 similar value
print(fruits.index("apples")) # result 2

# to add value in a lists
fruits.append("oranges") 
print(fruits)

# to combine list with other list
fruits.extend(years)
print(fruits)

# remove using exact match of the item
fruits.remove("oranges")
print(fruits)

# remove using item index number (start from 0)
fruits.pop(0)
print(fruits)

# remove by index number from the end
fruits.pop(-1)
print(fruits)

# to sort value ascending
numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()
print(numbers)

