message='It was a bright afternoon , nonetheless, it rained heavily causing torential floods'
count={}

for x in message:
    count.setdefault(x,0)
    count[x]+=1

print(count,'\n\n')



#to get a better view
import pprint
message='It was a bright afternoon , nonetheless, it rained heavily causing torential floods'
count={}

for x in message:
    count.setdefault(x,0)
    count[x]+=1

pprint.pprint(count)