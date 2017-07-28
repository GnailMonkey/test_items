# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:26:04 2016

@author: Laresh
"""

from collections import Counter
from math import sqrt
from decimal import Decimal
from itertools import combinations
import csv

class Finditempairs:
    def __init__(self):
        self.file_path = raw_input('please input the file path:\n')
        self.save_path = r'E:\python_demo\rou_calc.csv'

    def get_index(self, content):
        # 事务总量
        total = len(content)
        # k:题号,v:次数
        all_items = {}
        # 所有题号
        answers = []
        for i in range(total):
            content[i] = content[i][10:].strip()
            temp = []
            for m, n in enumerate(content[i], start=1):
                if int(n) == 0:
                    temp.append(m)
                    all_items[m] = all_items.setdefault(m, 0) + 1
            answers.append(temp)
        return answers, all_items, total

    def freq_2(self, answers, all_items):
        all_pairs = []
        all_pairsdict = {}
        for item in answers:
            temp = list(combinations(item, 2))
            all_pairs.extend(temp)
        for pair in all_pairs:
            all_pairsdict[pair] = all_pairsdict.setdefault(pair, 0) + 1
        return all_pairsdict
    
    '''
    write the correlative record(ρ>0) into csv file, calculate the ρ. 
    '''
    def csv_write(self, answer_con, record_len):
        csvfile = file(self.save_path, 'wb')
        writer = csv.writer(csvfile)
        writer.writerow(['Num', 'Occu', 'Num', 'Occu', 'Corr_oc', 'Sup', 'Rho'])
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

    def run(self):
        try:
            with open(self.file_path) as f:
                content = f.readlines()
        except IOError as err:
            print 'File Error:' + str(err)
        answers, all_items, total = self.get_index(content)
        all_pairsdict = self.freq_2(answers, all_items)
        self.csv_write(total, all_pairsdict, all_items)
        print 'file successfully written!'

if __name__ == '__main__':
    ip = Finditempairs()
    ip.run()
