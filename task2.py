import json
file=open("task_1_movie_top.json","r")
a=file.read()
data=json.loads(a)
i=0
while i<len(data):
    j=0
    while j<len(data):
        if data[i]["year"]<data[j]["year"]:
            d=data[i]
            data[i]=data[j]
            data[j]=d
        j+=1
    i+=1
dict1={}
i=0
while i<len(data):
    list=[]
    j=0
    while j<len(data):
        if data[i]["year"]==data[j]["year"]:
            list.append(data[j])
        j+=1
    dict1[data[i]["year"]]=list
    i+=1
with open ("task_2_serial wise year.json","w")as f:
    json.dump(dict1,f,indent=4)       