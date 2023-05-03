#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
# sort items by value and get top 10
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
sorted_data = sorted(items[:10], key=lambda item: item[1], reverse=False)

# extract x, y, and label values
x = range(len(sorted_data))
y = [item[1] for item in sorted_data]
label = [item[0] for item in sorted_data]

# create bar plot
plt.bar(x, y)

# set x-axis ticks and labels
plt.xticks(x, label)

# set axis labels
plt.xlabel("Country")
plt.ylabel("Tweet Volume")

# set font family for plot title
plt.rcParams['font.family'] = 'Arial'

# save plot
plt.savefig("covidcountrykor.png")

# display plot
plt.show()
