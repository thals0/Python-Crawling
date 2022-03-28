import csv
f=open("./example.csv",'w',newline='',encoding="utf-8-sig")
wtr=csv.writer(f)

wtr.writerow(['이름','나이','언어'])

name_list =['길동','철수','영희']
age_list=[10,20,30]
lan_list=['파이썬','C','JAVA']

for i in range(3):
    name=name_list[i]
    age=age_list[i]
    language=lan_list[i]
    wtr.writerow([name,age,language])

f.close()
