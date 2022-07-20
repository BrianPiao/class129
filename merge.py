import csv
dataset_1 = []
dataset_2 = []
with open("dataset_1.csv") as f:
    c = csv.reader(f)
    for a in c:
        dataset_1.append(a)
with open("dataset_sorted.csv") as f:
    c = csv.reader(f)
    for e in c:
        dataset_2.append(e)
header1 = dataset_1[0]
planetdata1 = dataset_1[1:]
header2 = dataset_2[0]
planetdata2 = dataset_2[1:]
header = header1+header2
planetdata = []
for index, data_row in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
#a+ creates new file/opens existing file for reading/writing &file pointer position at the eof
with open("final.csv","a+") as f:
    c = csv.writer(f)
    c.writerow(header)
    c.writerows(planetdata)