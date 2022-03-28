import csv
f=open('./covid19_articles.csv','r')
rdr=csv.reader(f)

count=0
for data in rdr:
    if '[속보]' in data[2]:
        print(data[2])
        count +=1

f.close()