import csv
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newData=[]
for i in range(len(filedata)):
    n_num=filedata[i][2]
    newData.append(float(n_num))

n=len(newData)
total=0
for x in newData:
    total+=x
mean = total/n

print("mean="+str(mean))
