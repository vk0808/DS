#!/usr/bin/env python
# coding: utf-8

# In[60]:


##Python 3 Script

import unicodecsv
from xlrd import open_workbook

f=open_workbook('Dummy.xlsx')
r = len(f.sheet_names())
for x in range(r):
    sh = f.sheet_by_index(x)
    filename = (sh.name+'.csv')
    print(filename)
    fh = open(filename,"wb")
    csv_out = unicodecsv.writer(fh, encoding='utf-8')
    for row_number in range(sh.nrows):
        csv_out.writerow(sh.row_values(row_number))
    fh.close()

