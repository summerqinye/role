import csv
import re
import json
import numpy as np
import scipy.stats
import scipy.special as special
from matplotlib import rcParams

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
# rcParams['text.usetex'] = True
rcParams['font.family'] = 'sans-serif'

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def readcsv(filename):
    csvFile = open(filename, encoding='utf-8')
    reader = csv.reader(csvFile)
    result = []
    for line in reader:
        if reader.line_num == 1:
            dict = line
            continue
        result.append({})
        for i in range(len(line)):
            result[-1][dict[i].strip()] = line[i].strip()
    csvFile.close()
    return result

def to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

def cohend(x1, x2):
    s1 = np.std(x1)
    s2 = np.std(x2)
    n1 = len(x1)
    n2 = len(x2)
    s = ( ((n1-1)*s1*s1 + (n2-1)*s2*s2) / (n1+n2-2)  ) ** 0.5
    return abs(np.mean(x1)-np.mean(x2)) / s

def get_stats(data):
    stats = {}
    for d in data:
        options = d.split(";")
        for d in options:
            d = d.rstrip().lstrip()
            if d not in stats.keys(): stats[str(d)] = 0
            stats[str(d)] += 1
    return stats

def get_data(res, target, constraints = {}):
    data = []
    # for i in range(1,4): constraints["AC"+str(i)] = "Strongly Agree" # Attention check

    for row in res:
        flag = True
        for k in constraints.keys():
            if k in row.keys() and constraints[k] != row[k]:
                flag = False
        if not flag:
            continue
        data.append(row[target])
    return data
