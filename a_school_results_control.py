
def control():

    print('1: ENTER STUDENTS RESULTS')
    print('2: ADD MORE STUDENTS RESULTS')
    print('3: EDIT THE RESULTS OF A PARTICULAR STUDENT')
    print('4: ACCESS A STUDENTS RESULTS')
    print('5: DELETE RESULTS OF A PARTICULAR STUDENT')


    decision=int(input('Enter the number representing your choice to continue: '))
    if decision ==1:
        import a_school_results_entry_system_replica
    elif decision==2:
        import a_school_results_append
    elif decision==3:
        import a_school_results_edit
    elif decision==4:
        import a_school_results_reading    
    elif decision==5:
        import a_school_results_delete
    else:
        print('ERROR!! Inappropriate choice entered')
        control()

control()