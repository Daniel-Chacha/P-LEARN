
for x in range(num):
    h=int(input('FILE.NO: '))

    while h in file_no:
        print('ERROR!! The FileNo already exists in another entry')
        print('Re-enter the FileNo')
        h=int(input('Enter FILENo. '))
    file_no.append(h)
    a=(input('NAME: '))
    names.append(a)

start_entry={
    'FILE_NO.' :file_no,
    'NAMES'  :names
}
df1=pd.DataFrame(start_entry)
df1.index+=1

def subject_choice():
    k=input('Enter name of subject to key in results: ')
    sub_choice=k.lower()
    if sub_choice == 'mathematics':
        sub_selected=math
    elif sub_choice == 'english':
        sub_selected=eng
    elif sub_choice == 'kiswahili':
        sub_selected=kisw
    elif sub_choice == 'chemistry':
        sub_selected= chem
    elif sub_choice == 'biology':
        sub_selected=bio
    elif sub_choice == 'physics':
        sub_selected=phyc
    elif sub_choice == 'geography':
        sub_selected=geo
    elif sub_choice == 'computer':
        sub_selected=comp
    else:
        print('ERROR!! Wrong Entry, Re-enter your choice')
        subject_choice()

   
    x=1
    while x<= len(df1):
        print(df1.loc[[x]])
        a=int(input(("Enter student's mark: ")))
        sub_selected.append(a)
        x+=1
    
    def another_subject():
        print('Do you want to enter marks for another subject? ')
        des=input('YES or NO: ')
        des1=des.lower()
        if des1 == 'yes':
            subject_choice()
        elif des1=='no':
            print(f'Marks entry for {sub_choice} completed.')
        else:
            print('Wrong choice entered!! Re-try')
            another_subject()
    another_subject()

subject_choice()

for e in range(num):
    t=0
    if math:
        t+=math[e]
    if eng:
        t+=eng[e]
    if kisw:
        t+=kisw[e]
    if chem:
        t+=chem[e]
    if bio:
        t+=bio[e]
    if phyc:
        t+=phyc[e]
    if geo:
        t+=geo[e]
    if comp:
        t+=comp[e]

    total.append(t)
    avg=t/8
    average.append(avg)
    w=grading(avg)
    grade.append(w)




for x in range(num):
    h=int(input('FILE NUMBER: '))

    while h in new_file:
        print('ERROR!! The FileNo already exists in another entry')
        print('Re-enter the FileNo')
        h=int(input('Enter FILE NUMBER: '))
    while h in file_no:
        print('ERROR!! You already entered the file number')
        print('Re-enter the File Number')
        h=int(input('Enter FILE NUMBER: '))
