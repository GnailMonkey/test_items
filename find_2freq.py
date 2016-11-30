# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:26:04 2016

@author: Laresh
"""

from collections import Counter
from math import sqrt
from decimal import Decimal
import csv

def get_index(content):
    length = len(content)
    record = []
    answer = []
    for i in range(length):
        content[i] = content[i][10:].strip()
        temp = []
        for m,n in enumerate(content[i],start=1):
            if int(n) == 0:
                temp.append(m)
        answer.extend(temp)
        record.append(temp)
    return answer, record

def freq_2(answer, record):
    count = 0
    answer_pair = []
    answer_con = []
    record_len = 0
    for item in record:
        l = len(item)
        for i in range(l):
            for j in range(i+1, l):
#                t = ','.join([str(item[i]),str(item[j])])
                t = '%s,%s' %(item[i],item[j])
                answer_pair.append(t)
        record_len += 1            
    answer_count = Counter(answer).most_common()
    answer_pair_count = Counter(answer_pair).most_common()
    for kv in answer_pair_count:
        pair = kv[0].split(',')
        temp = []
        for i in answer_count:
            print type(i[0])
            if str(i[0]) in pair:
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
    csvfile = file(r'f:\another_test\rou_calc.csv','wb')
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
        if bottom_value != 0:
            rou = Decimal(up_value/bottom_value).quantize(Decimal('0.00'))
        else:
            rou = 0
        data = [na,ta,nb,tb,tab,sup,rou]
        writer.writerow(data)
    csvfile.close()

def main():
    path = raw_input('please input the file path:\n')
    try:
        with open(path) as f:
            content = f.readlines()
    except IOError as err:
        print 'File Error:' + str(err)
    answer, record = get_index(content)
    answer_con, record_len = freq_2(answer, record)
    csv_write(answer_con, record_len)
    print 'file successfully written!'

if __name__ == '__main__':
    main()
    
                
   