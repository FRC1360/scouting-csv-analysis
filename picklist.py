import csv
from sys import argv

climbWeight = float(argv[2])
gearsWeight = float(argv[3])

with open(argv[1], 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data2 = {}


def tryInt(value):
    try:
        return int(value)
    except:
        return 0
    pass


for entry in data:
    if entry[2] == '':
        continue
    if not entry[2] in data2:
        data2[entry[2]] = [entry[2], 1 if entry[11] == 'Yes' else 0, tryInt(entry[9]), 0, 0, 1, 0]
    else:
        x = data2[entry[2]]
        if entry[11] == 'Yes':
            x[1] += 1
        x[2] += tryInt(entry[9])
        x[5] += 1

for team in data2.values():
    team[3] = team[1] / team[5]
    team[4] = team[2] / team[5]
    team[6] = climbWeight * team[3] + gearsWeight * team[4]


def sgn(value):
    return (value > 0) - (value < 0)


print('\n'.join([','.join(str(x) for x in team) for team in sorted(data2.values(), key=lambda entry: entry[6], reverse=True)]))
