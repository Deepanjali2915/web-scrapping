import json
def  movie_directors():
    file2=open("task_5_my_file_.json","r")
    h=json.load(file2)
    # print(h)
    list=[]
    for i in h:
        # print(i)
        # print(i["Original Language:"])
        if i["Original Language:"]not in list:
            list.append(i["Original Language:"])
            # print(list)
            # print(i[])
    dict8={}
    list9=[]
    for k in list:
        i=0
        count=0
        while i<len(h):
            if k==h[i]["Original Language:"]:
                # print(k)
                count+=1
            i+=1
        dict8.update({k:count})
        print(dict8)
    list.append(dict8)
    # print(list)
    with open("task_6.json","w")as file:
        json.dump(list,file,indent=4)
    return list
movie_directors()
