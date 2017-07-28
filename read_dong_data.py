# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:53:35 2016

@author: Laresh
"""
from math import sqrt
from decimal import Decimal
from itertools import combinations
import csv
import pandas as pd
 
def get_index(table):
    total = len(table)
    columns = len(table.columns)
    # k:题号,v:次数
    all_items = {}
    # 所有题号
    answers = []
    for i in range(total):
        temp = []
        for j in range(4, columns+1, 2):
            score = table.iloc[i, j]
            if score < 0:
                test_num = table.iloc[i, j-1]
                temp.append(test_num)
                all_items[test_num] = all_items.setdefault(test_num, 0) + 1
        if temp:
            answers.append(temp)
    return answers, all_items, total
 
def freq_2(answers, all_items):
    all_pairs = []
    all_pairsdict = {}
    for item in answers:
        temp = list(combinations(item, 2))
        all_pairs.extend(temp)
    for pair in all_pairs:
        all_pairsdict[pair] = all_pairsdict.setdefault(pair, 0) + 1
    return all_pairsdict

'''
write the correlative record into csv file, calculate the rho. 
'''

def csv_write(total, all_pairsdict, all_items):
    csvfile = file(r'C:\Users\Administrator\Desktop\data.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['Num', 'Occu', 'Num', 'Occu', 'Corr_oc', 'Rho'])
    for k, v in all_pairsdict.iteritems():
        if k[0] in all_items.keys() and k[1] in all_items.keys():
            up_value = v*total-all_items[k[0]]*all_items[k[1]]
            bottom_value = sqrt(all_items[k[0]]*(total-all_items[k[0]])* \
            all_items[k[1]]*(total-all_items[k[1]]))
            if bottom_value != 0 and up_value >= 0:
                rou = Decimal(up_value/bottom_value).quantize(Decimal('0.00'))
                data = [k[0], all_items[k[0]], k[1], all_items[k[1]], v, rou]
                writer.writerow(data)
    csvfile.close()
 
def main():
    path = r'C:\Users\Administrator\Desktop\a.xls'
    table = pd.read_excel(path, sheetname=0, header=0, encoding='utf-8')
    answers, all_items, total = get_index(table)
    all_pairsdict = freq_2(answers, all_items)
    csv_write(total, all_pairsdict, all_items)
    print 'file successfully written!'
 
if __name__ == '__main__':
    main()
            
   
