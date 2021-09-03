from collections import Counter
import csv
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newData=[]
for i in range(len(filedata)):
    n_num=filedata[i][2]
    newData.append(float(n_num))

data = Counter(newData)
modeData = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0
    }    

for weight,occurrence in data.items():
    if 75<float(weight)<85:
        modeData["75-85"]+=occurrence

    elif 85<float(weight)<95:
        modeData["85-95"]+=occurrence

    elif 95<float(weight)<105:
        modeData["95-105"]+=occurrence

    elif 105<float(weight)<115:
        modeData["105-115"]+=occurrence

    elif 115<float(weight)<125:
        modeData["115-125"]+=occurrence   
    
    elif 125<float(weight)<135:
        modeData["125-135"]+=occurrence

    elif 135<float(weight)<145:
        modeData["135-145"]+=occurrence

    elif 145<float(weight)<155:
        modeData["145-155"]+=occurrence

    elif 155<float(weight)<165:
        modeData["155-165"]+=occurrence   

    elif 165<float(weight)<175:
        modeData["165-175"]+=occurrence


modeRange,modeOccurrence = 0,0
for range,occurrence in modeData.items():
    if occurrence>modeOccurrence:
        modeRange,modeOccurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence
mode=float((modeRange[0]+modeRange[1])/2)

print("mode is ",mode)
           
    
