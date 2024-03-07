import csv
import openpyxl

file_path = input('\n#> Enter the file path or name of the file : ').replace('"','')
t = len(file_path)
if file_path[t-4:] != '.csv':
    file_path += '.csv'


t = len(file_path)
save_name = file_path[0:t-4] + '.xlsx'


#>> This block enables you to choose a different file name for your extracted '.xlsx' file
# save_name = input('\n#> Enter the name of file to be saved : ')
# t = len(save_name)
# if save_name[t-5:] != '.xlsx':
#     save_name += '.xlsx'

csv_file = open(file_path,'r')
data = csv.reader(csv_file)

next = 1
workbook = openpyxl.Workbook()
sheet = workbook.active
c_Name = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for row in data:
    if next == 1:
        c = len(row)
    for i in range(1,c+1):
        t = str(next)
        sheet[c_Name[i-1]+t] = row[i-1]
    next += 1

workbook.save(save_name)

print('\n ※ Your file has been converted successfully!\n   ⁘ ".xlsx" file has been saved in the original file directory.\n')
