import csv

data = []
with open('clouds.dat') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        data.append(row)

keys = data[0].keys()
data = {k: [float(data[i][k]) for i in range(len(data))] for k in keys}

def median(l):
    return sorted(l)[ (len(l) + 1) // 2 ]

print ({k: median(data[k]) for k in keys})