# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:34:58 2016

@author: Laresh

读取高一物理所有学生的客观选择题，并拿到做对或做错题号
"""
import os
import pandas as pd

count = 0
df = pd.DataFrame()
path = 'excel'
list_file = os.listdir(path)

for f in list_file:
    f = f.decode('gb2312').encode('utf-8')
    f_path =  path+ '\\' + f
    uipath = unicode(f_path , "utf8")
    excel_read = pd.ExcelFile(uipath)
    table = excel_read.parse('Sheet1')
    # 拿到选择题的列，并将3分替换成1分
    table = table.iloc[:,7:23]
    table = table.replace(3,1)
    df = df.append(table)
    count += 1
    print f + ' 读取成功'
print '一共有%d个文件' % count
df.to_csv('test.csv',encoding='utf-8', index=False)
print 'csv文件写入成功'

txt_file = open('test.txt','w')
with open('test.csv') as f:
    content = f.readlines()
    content = content[1:]
    for i in range(len(content)):
        temp = []
        content[i] = content[i].replace(',','').strip()
        for m,n in enumerate(content[i], start=1):
            if int(n) == 0:
                temp.append(m)
        rec = ''.join(str(temp)).replace('[','').replace(']','').replace(',','')
        txt_file.writelines(rec)
        txt_file.writelines('\n')
print '输出txt文件成功'
txt_file.close()
        
        
