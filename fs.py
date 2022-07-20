##Data preprocessing is the process of transforming raw data into an understandable format.
import csv
data = []
with open("dataset_2.csv") as f:
    c = csv.reader(f)
    for a in c:
        data.append(a)
headers = data[0]
planetdata = data[1:]
for e in planetdata:
    e[2] = e[2].lower()
planetdata.sort(key = lambda planetdata:planetdata[2])
#a+ creates new file/opens existing file for reading/writing &file pointer position at the eof
with open("dataset_sorted.csv","a+") as f:
    c = csv.writer(f)
    c.writerow(headers)
    c.writerows(planetdata)