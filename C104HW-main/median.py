import csv
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

#print(filedata)

filedata.pop(0)
newData=[]
for i in range(len(filedata)):
    n_num=filedata[i][2]
    newData.append(float(n_num))

n=len(newData)
newData.sort()  

if(n%2==0):
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median1+median2)/2

else:
    median=float(newData[n//2])

print("median is"+str(median))


