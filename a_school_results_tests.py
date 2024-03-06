import pandas as pd

models=['volvo','bmw']
years=['2024','2023']
countrys=['kenya','tz']

dict={
    'model':models,
    'year': years,
    'country':countrys
}
df1=pd.DataFrame(dict)
df1.index+=1

models=['mercedes','ferari']
years=['2022','2021']
countrys=['uganda','rwanda']
dict2={
    'model':models,
    'year': years,
    'country':countrys
}
df2=pd.DataFrame(dict2)
x=pd.concat([df1,df2],ignore_index=True)
x.index+=1

print(x)
print('\n\n')
j=x.drop
print(j)

print(df1)