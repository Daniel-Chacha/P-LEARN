#sorting alphabetically
thislist=['orange','mango','kiwi', 'pineapple', 'banana']
thislist.sort()
print(thislist)

#sorting numerically in ascending order
thislist=[100,50,65,82,23]
thislist.sort()
print(thislist)

#sorting in descending order; use the keyword 'reverse=True'
thislist=['orange','mango','kiwi', 'pineapple', 'banana']
thislist.sort(reverse=True)
print(thislist)


thislist=[100,50,65,82,23]
thislist.sort(reverse=True)
print(thislist)

print('-----------------------------------------\n')
#customize sort function; by using the keyword 'key=myfunc';sort the number based on how close the number is to 50
def myfunc(n):
    return abs(n-50)

thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

print('-----------------------------------------\n')
#by default , the sort() method is case sensitive ,resulting in all capital letters being sorted before lowercase letters
thislist=['banana','Orange','Kiwi','cherry']
thislist.sort()
print(thislist)

#case insensitive sorting; using the keyword 'key=str.lower'
thislist=['banana','Orange','Kiwi','cherry']
thislist.sort(key=str.lower)
print(thislist)

print('-----------------------------------------\n')
#to reverse the order of a list ,regardless of the alphabet
thislist=['banana','Orange','Kiwi','cherry']
thislist.reverse()
print(thislist)