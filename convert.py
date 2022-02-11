import pandas as pd
import glob
import os
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# location = 'C:\\Users\\Sam\\Desktop\\pipeline_export\\*.csv'
# csv_files = glob.glob(location)
csv_files = './pipeline_export.csv'

df1 = pd.DataFrame()

df2 = pd.read_csv(csv_files)
df1 = pd.concat([df1, df2])

# df1['Name'] = df2['First Name'] + ' ' + df2['Last Name']
df1['Name'] = '=HYPERLINK(' '"' + df2['Profile URL'] + '"' + \
    ',' + '"' + df2['First Name'] + ' ' + df2['Last Name'] + '"' + ')'
df1.insert(0, 'Full Name', df1['Name'])
del df1['Last Name']
del df1['First Name']
del df1['Name']
del df1['Profile URL']
df1 = df1.fillna('')
df1.to_excel("C:\\Users\\Sam\\Desktop\\convertedexport.xlsx")
