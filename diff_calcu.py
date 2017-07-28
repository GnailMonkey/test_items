# -*- coding:utf-8 -*-
from decimal import Decimal
import pandas as pd
import csv
 
def get_index(table):
    row = len(table)
    column = len(table.columns)
    test_dict = {}
    wrong_dict = {}
    for i in range(row):
        for j in range(3, column, 2):
            item = table.iloc[i, j]
            test_dict[item] = test_dict.setdefault(item, 0) + 1
    for m in range(row):
        for n in range(4, column+1, 2):
            score = table.iloc[m, n]
            if score < 0:
                test_item = table.iloc[m, n-1]
                wrong_dict[test_item] = wrong_dict.setdefault(test_item, 0) + 1
    return test_dict, wrong_dict
 
# 难度=试题答错人数/该试题作答总人数
def csv_write(test_dict, wrong_dict):
    csvfile = file(r'C:\Users\Administrator\Desktop\test_diff.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['Num', 'Wrong', 'All', 'Diff'])
    for k, v in wrong_dict.iteritems():
        if k in test_dict.keys():
            diff = Decimal(v*1.0/test_dict[k]).quantize(Decimal('0.00'))
            data = [k, v, test_dict[k], diff]
            writer.writerow(data)
    csvfile.close()
 
def main():
    path = r'C:\Users\Administrator\Desktop\a.xls'
    table = pd.read_excel(path, sheetname=0, header=0, encoding='utf-8')
    test_dict, wrong_dict = get_index(table)
    csv_write(test_dict, wrong_dict)
    print 'file successfully written!'
 
if __name__ == '__main__':
    main()
