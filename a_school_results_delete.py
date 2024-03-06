import pandas as pd 

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

    #print('Enter yes to delete or no to exit')
    def confirm_deletion():
        a=input("Enter 'yes' to delete or 'no' to exit: ")
        option=a.lower()
        #print(matching_row)
        if option =='yes':
            new_df=df.drop(matching_row.index)
            print(new_df)
            from a_school_results_entry_system_replica import excel_file
            l=excel_file(new_df)
            #new_df.to_excel('a-results2.xlsx',index=False)
        elif option =='no':
            print('EXITING WITHOUT DELETING')
            studentresult()
        else:
            print("Invalid Input: Please enter 'yes' or 'no' ")
            confirm_deletion()  
    confirm_deletion()
    

studentresult()