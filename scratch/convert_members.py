import csv
import json

infile = './LtU membership (for website) - Sheet1.tsv'
outfile = '../_data/members.yml'

with open(infile, 'r') as tsv_file:
    data = list(csv.DictReader(tsv_file, delimiter='\t'))

with open(outfile, 'w') as json_file:
    json.dump(data, json_file, indent=4)
