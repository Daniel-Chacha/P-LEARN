def excel_file(df):
    sorted=df.sort_values(by='TOTAL',ascending=False)
    sorted['RANK']=sorted['TOTAL'].rank(ascending=False,method='dense')

    #a file and pass the dataframe to it
    with pd.ExcelWriter('a-results2.xlsx',engine='openpyxl',mode='w')as file:
        sorted.to_excel(file,index=False,startrow=0,startcol=0,sheet_name='sheet1')

    newsubtotal=['SubjectTotal','-',subject_total[0],subject_total[1],subject_total[2],subject_total[3],subject_total[4],subject_total[5],subject_total[6],subject_total[7],subject_total[8],subject_total[9],'-']
    extra1=pd.DataFrame([newsubtotal],columns=df.columns)
    sorted=sorted._append(extra1, ignore_index=True)

    newgrand_avg=['SubjectAverage','-',subject_avg[0],subject_avg[1],subject_avg[2],subject_avg[3],subject_avg[4],subject_avg[5],subject_avg[6],subject_avg[7],subject_avg[8],subject_avg[9],'-']
    extra2=pd.DataFrame([newgrand_avg],columns=df.columns)
    sorted=sorted._append(extra2, ignore_index=True)

    newgrand_grade=['SubjectGrades','-',subject_grade[0],subject_grade[1],subject_grade[2],subject_grade[3],subject_grade[4],subject_grade[5],subject_grade[6],subject_grade[7],subject_grade[8],subject_grade[9],'-']
    extra3=pd.DataFrame([newgrand_grade],columns=df.columns)
    sorted=sorted._append(extra3, ignore_index=True)

    sorted.index+=1

    #creating an excel workbook and passing the dataframe to it

    with pd.ExcelWriter('a-results3.xlsx',engine='openpyxl',mode='w') as writer:
            sorted.to_excel(writer,index=False,startrow=4,startcol=0,sheet_name='Sheet1')

    #call the file and append additional text above the table

    wb=openpyxl.load_workbook('a-results3.xlsx')
    ws=wb.active

    c=[['A1','N1'],['A2','N2'],['A3','N3'],['A4','N4']]
    s=['HIDDENVILLE  HIGHSCHOOL','FORM 3 NORTH','TERM  2','']
    for start_cell,end_cell in c:
        ws.merge_cells(f'{start_cell}:{end_cell}')
        cell=ws[start_cell]
        cell.alignment=Alignment(horizontal='center',vertical='center')
    
    ws['A1'].value='HIDDENVILLE  HIGHSCHOOL'
    ws['A1'].font=Font(size=21)
    ws['A2'].value='FORM 3 NORTH'
    ws['A2'].font=Font(size=17)
    ws['A3'].value='TERM  2'
    ws['A3'].font=Font(size=17)
    ws['A4'].value='MOCK  EXAM'
    ws['A4'].font=Font(size=17)

    wb.save('a-results3.xlsx')
    
excel_file(df)