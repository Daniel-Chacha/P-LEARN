#check if the text start with 'The' and end in 'Spain'
import re
txt='The rain in Spain'
x=re.search('^The.*Spain$',txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")