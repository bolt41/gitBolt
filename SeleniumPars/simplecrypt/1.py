all = dict()
for i in range(1,12):
    all[str(i)] = [0 , 0]
with open('dataset_3380_5.txt') as f:
    for line in f:
        line = line.strip().split()
        all[line[0]][0] += 1
        all[line[0]][1] += int(line[2])
for key,el in all.items():
    if el[0] == 0:
        print(key + '-')
    else:
        print(key, el[1]/el[0])