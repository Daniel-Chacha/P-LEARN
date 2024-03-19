
a=['Today','is','quite','cold','though','it','is','sunny']
b=','.join(a)
print(f" '{b}' \n\n")

#split
c='Today is quite cold though it is sunny' 
d=c.split()
print(d,'\n\n')

#split() is commonly used to slpit a multiline string characters
e='''
How have you been?
Personally am fine.
I forgot my key at your place this morning.
Kindy carry it , I will pass by to pick it anytime.

Regards
Daniel
'''

f=e.split('\n')
print(f)