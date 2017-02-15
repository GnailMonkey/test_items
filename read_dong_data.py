# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:53:35 2016

@author: Laresh
"""
from collections import Counter
from math import sqrt
from decimal import Decimal
from itertools import combinations
import csv
import pandas as pd

#excel_read = pd.ExcelFile(r'C:\Users\Administrator\Desktop\exercise2_ans_history.xls')

def get_index(table):
    r = len(table)
    c = len(table.columns)
    answer = []
    record = []
    for i in range(r):
        temp = []
        for j in range(4,c+1,2):
            t=table.iloc[i,j]
            if t < 0:
                s=table.iloc[i,j-1]
                temp.append(s)
        if temp:
            answer.extend(temp)
            record.append(temp)
    return answer, record

def freq_2(answer, record):
    count = 0
    answer_pair = []
    answer_con = []
    record_len = 0
    for item in record:
        temp = list(combinations(item,2))
        answer_pair.extend(temp)
        record_len += 1            
    answer_count = Counter(answer).most_common()
    answer_pair_count = Counter(answer_pair).most_common()
    for kv in answer_pair_count:
        temp = []
        for i in answer_count:
            if i[0] in kv[0]:
                temp.append(i)
                count += 1
                if count == 2:
                    temp.append(kv)
                    count = 0
                    answer_con.append(temp)
    return answer_con, record_len
'''
write the correlative record into csv file, calculate the rho. 
'''
def csv_write(answer_con, record_len):
    csvfile = file(r'f:\another_test\real_data.csv','wb')
    writer = csv.writer(csvfile)
    writer.writerow(['Num','Occu','Num','Occu','Corr_oc','Sup','Rho'])
    for con in answer_con:
        na = con[0][0]
        nb = con[1][0]
        ta = con[0][1]
        tb = con[1][1]
        tab = con[2][1]
        sup = Decimal(1.0*tab/record_len).quantize(Decimal('0.00'))
        up_value = tab*record_len - ta*tb
        bottom_value = sqrt(ta*(record_len - ta)*tb*(record_len - tb))
        if bottom_value != 0 and up_value >=0 and tab >= 5:
        # if bottom_value != 0 and up_value >= 0:
            rou = Decimal(up_value/bottom_value).quantize(Decimal('0.00'))
            data = [na,ta,nb,tb,tab,sup,rou]
            writer.writerow(data)
    csvfile.close()

def main():
    path = raw_input('please input the file path:\n')
    table = pd.read_excel(path,sheetname=0,header=0,encoding='utf-8')
    answer, record = get_index(table)
    answer_con, record_len = freq_2(answer, record)
    csv_write(answer_con, record_len)
    print 'file successfully written!'

if __name__ == '__main__':
    main()

            
   