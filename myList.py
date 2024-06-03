# list slicing => to make a copy of a list
myNumbers=[1,2,3,4,5,6,7,8,9]
# some_list[start:end:step]
selectedNumbersFromList=myNumbers[1:6:1]
print(selectedNumbersFromList)
selectedNumbersFromList=myNumbers[-5:]
print(selectedNumbersFromList)
print("-----------------------------------")
copyOfNumbers=myNumbers[:]
print(copyOfNumbers)
print(myNumbers==copyOfNumbers)
print(myNumbers is copyOfNumbers)
print("-----------------------------------")
colors=["red","green","blue","yellow","orange"]
copyOfColors=colors[::-1]
colors.reverse()
print(colors)
print(copyOfColors)
print("-----------------------------------")
myName="mohammad"
print(myName[::-1])