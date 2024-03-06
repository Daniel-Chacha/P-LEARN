ages=[]
for k in range(5):
    elements=int(input('The ages for the students are: '))
    ages.append(elements)

total_ages=sum(ages)
average=total_ages/5
print('The sum of the ages is: ',total_ages)
print('The average age is: ',average)

oldest=max(ages)
youngest=min(ages)

print('The oldest student is ',oldest,'years old')
print('The youngest student is ',youngest,'years old')
