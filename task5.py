from task1 import adventure_movie
import json
from bs4 import BeautifulSoup
import requests
scrapped=adventure_movie()
def get_movie_list_details(movies): 
    j=0
    list4=[]
    # while j<len(movies):
    while j<20:
        url=movies[j]["movie_url"]
        print(url)
        x=requests.get(url)
        soup=BeautifulSoup(x.text,"html.parser")
        # html parser return text format
        movie_find_2=soup.find("ul",class_="content-meta info")
        movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")
        my_dict={}
        for i in movie_find_3:
            alldata=i.find("div",class_="meta-label subtle").get_text().strip()
            allvalue=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
            my_dict.update({alldata:allvalue})
        list4.append(my_dict)
        # print(list4)
        j+=1
    with open("task_5_my_file_.json","w")as f:
        json.dump(list4,f,indent=4)
    return list4
task5_data=get_movie_list_details(scrapped)
