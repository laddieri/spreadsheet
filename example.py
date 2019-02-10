import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
column_list = ['#','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH']

credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheetexample-231320-6775422787e9.json',scope)

gc = gspread.authorize(credentials)

sheetname = input('Enter the title of the google sheet: ')
user_choice = input("\nSelect what you'd like to do:\n\n1)Split a column that has Lastname, Firstname\n\n2)Combine separate first and last name columns into one column of Lastname, Firstname\n\nEnter the number of your selection:  ")

wks = gc.open(sheetname).sheet1

def split_full_names():

    name_column_name = input("Enter the letter name of the column that you'd like to split: ")
    name_column_number = column_list.index(name_column_name)
    output_column_name = input("Enter the letter name of the destination column (leave blank to add a new column): ")
    print(output_column_name)
    newnames=[]

    listofnames = wks.col_values(name_column_number)

    for x in range(1,len(listofnames)):
        nameparts = listofnames[x].split(", ")
        newnames.append(nameparts[1] + ' ' + nameparts[0])

    if output_column_name=='':
        wks.add_cols(1)

        last_col = wks.col_count
        output_column_name = column_list[last_col]

    cell_list = wks.range(f'{output_column_name}1:{output_column_name}{len(newnames)+1}')
    y=0
    for cell in cell_list:
        if y==0:
            cell.value = 'Formatted Names'
        else:
            cell.value = newnames[y-1]
        y+=1
    wks.update_cells(cell_list)

if user_choice =='1':
    split_full_names()
else:
    pass
