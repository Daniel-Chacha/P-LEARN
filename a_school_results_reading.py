#reading a student's result using the file number
import pandas as pd 
import matplotlib.pyplot as plt

def studentresult():
    search_value=int(input('Enter the File Number of the Student: '))

    df=pd.read_excel('a-results2.xlsx')
    #print(df)
    df.index+=1
    column_name='FILE_NO.'


    matching_row=df[df[column_name]==search_value]
    if matching_row.empty:
        print(f"There is no match of the File Number {search_value}")
        studentresult()
    else:
        z=matching_row.index[0]
        #print(z)
        print(df.loc[[z]])

        #bar plots of each student with their scores in each subject
        sub_names=['MATH','ENG','KISW','CHEM','BIO','PHYC','GEO','COMP']
        points=[]
        points.clear()
        t=df.loc[z]
        l=t['NAMES']
        m=t['MATH']
        points.append(m)
        n=t['ENG']
        points.append(n)
        o=t['KISW']
        points.append(o)
        p=t['CHEM']
        points.append(p)
        q=t['BIO']
        points.append(q)
        r=t['PHYC']
        points.append(r)
        s=t['GEO']
        points.append(s)
        u=t['COMP']
        points.append(u)
        plt.bar(sub_names,points)
        plt.xticks(rotation=45)
        plt.title(l)
        plt.tight_layout()
        #plt.savefig('a-results2-studentsbars.png')
        plt.show()

def subjectresults():
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
        subjectresults()
    df=pd.read_excel('a-results2.xlsx')
    df.index+=1
    selected_columns=df[['FILE_NO.','NAMES',search_column]]
    print(selected_columns)
    

    #yplots_titles=[['MATH','MATHEMATICS'],['ENG','ENGLISH'],['KISW','KISWAHILI'],['CHEM','CHEMISTRY'],['BIO','BIOLOGY'],['PHYC','PHYSICS'],['GEO','GEOGRAPHY'],['COMP','COMPUTER STUDIES']]
    df=pd.read_excel('a-results2.xlsx')
    plt.bar(df['NAMES'],df[search_column])
    plt.xticks(rotation=80)
    n_subchoice=sub_choice.upper()
    plt.title(n_subchoice)

    plt.tight_layout()
    #plt.savefig('a-results2-subjectsbars.png')
    plt.show()

def entry():
    print(" 1...ACCESS A SPECIFIC STUDENT'S RESULTS")
    print(' 2...ACCESS THE RESULTS OF A SUBJECT')
    choice=int(input('Enter  the number of your choice to proceed: '))
    if choice ==1:
       studentresult()
    elif choice==2:
       subjectresults()
    else:
       print('ERROR!! You entered a wrong choice, retry:')
       entry()

entry()