import pyodbc
import csv
import logging
import os.path
import writeCsv
# DESTINATION CONNECTION
 
my_cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; Trusted_Connection=yes')
my_cursor = my_cnxn.cursor()
save_here = 'C:/Users/bkt5031/Desktop/pythonAngular' 

 

def insert_records(table, yourcsv, cursor, cnxn):
    #INSERT SOURCE RECORDS TO DESTINATION
    with open(yourcsv) as csvfile:

        csvFile = csv.reader(csvfile, delimiter=',')

        print('File Read')
        logging.info('File Read')

        header = next(csvFile)
        headers = map((lambda x: x.strip()), header)
        insert = 'INSERT INTO {} ('.format(table) + ', '.join(headers) + ') VALUES '
        
         

        for row in csvFile:
            values = map((lambda x: "'"+x.strip()+"'"), row)
            my_cursor.execute(insert +'('+ ', '.join(values) +');' )
            my_cnxn.commit() #must commit unless your sql database auto-commits
            logging.info('Values Inserted') 
            print('Values Inserted')



table = '[STAGING].[dbo].TalismaLeadCards'
mycsv = 'export3.txt' # SET YOUR FILEPATH
insert_records(table, mycsv, my_cursor, my_cnxn)
writeCsv.writeNewCsv(mycsv)
my_cursor.close()
logging.info('Data Successfully Inserted')
print('Data Successfully Inserted')