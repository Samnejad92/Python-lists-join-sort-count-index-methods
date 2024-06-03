# index
myCourses=["Python","Kotlin","Ionic",
           "Python","JQuery","Vuejs","Python"]
index_kotlin=myCourses.index("Kotlin")
index_python=myCourses.index("Python",1)
print(index_python)
print("---------------------------------------")
# count
myCourses=["Python","Kotlin","Ionic",
           "Python","JQuery","Vuejs","Python"]
myNumbers=[1,2,3,4,5,6,7,8,9]
numberOfPython=myCourses.count("Python")
print(numberOfPython)
print("---------------------------------------")
# reverse
print(myNumbers)
myNumbers.reverse()
print(myNumbers)
print("---------------------------------------")
# sort
unOrderedNumbers=[5,9,6,3,18,75,1]
print(unOrderedNumbers)
unOrderedNumbers.sort()
print(unOrderedNumbers)
myCourses.sort()
print(myCourses)
print("---------------------------------------")
# join
secondCourses='-'.join(myCourses)
print(secondCourses)