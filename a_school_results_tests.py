import pandas as pd     

print("subject selection available include:")
print(' Mathematics , English ,Kiswahili, Chemistry, Biology, Physics, Geography, Computer')
k=input('Enter your choice: ')
sub_choice=k.lower()
if sub_choice == 'mathematics':
    search_column='MATH'
elif sub_choice == 'english':
    search_column='ENG'
elif sub_choice == 'kiswahili':
    search_column='KISW'
elif sub_choice == 'chemistry':
    search_column= 'CHEM'
elif sub_choice == 'biology':
    search_column='BIO'
elif sub_choice == 'physics':
    search_column='PHYC'
elif sub_choice == 'geography':
    search_column='GEO'
elif sub_choice == 'computer':
    search_column='COMP'
else:
    print('ERROR!! Wrong Entry, Re-enter your choice')
    edit_whole_class()
df1=pd.read_excel('a-results2.xlsx')
df1.index+=1
selected_columns=df1[['FILE_NO.','NAMES',search_column]]
#print(selected_columns)

print(selected_columns.loc[[0]])

p=int(input('Enter the new score: '))