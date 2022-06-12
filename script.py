pip install requests
pip install bs4

import requests
from bs4 import BeautifulSoup

#This function is used for image links extraction
def get_topic_imgs(content):
    selection_class = '_1fQZEK' 
    topic_imgs_tags = content.find_all('a', {'class': selection_class})
    topic_imgs = []
    for tag in topic_imgs_tags:
        if tag.img:topic_imgs.append(tag.img["src"])
    return topic_imgs


mb_name=[]
mb_price=[]
mb_configuration_details=[]
mb_images_link=[]

page_num = input('enter no. of pages')
for i in range(1,int(page_num)+1):
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=" + str(i)
    req=requests.get(url)
    content=BeautifulSoup(req.content,'html.parser')
    
    name=content.find_all('div',{"class":"_4rR01T"})
    price=content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
    configuration_details = content.find_all('span',{"class":"_2_R_DZ"}) 
    mb_images_link = get_topic_imgs(content)  
    battery = content.find_all('li',{"class":"rgWa7D"})[3].text
    
    
    for i in name:
        mb_name.append(i.text)
    for i in price:
        mb_price.append(i.text)
    for i in configuration_details:
        mb_configuration_details.append(i.text)
        
print(len(mb_name))
print(len(mb_price))
print(len(mb_images_link))
print(len(mb_configuration_details))

import pandas as pd
df=pd.DataFrame({'Product Name':mb_name,'configuration_details':mb_configuration_details,'image_links':mb_images_link,'Price':mb_price})

print(df)  #it will print csv file

df.to_excel(r'C:\Users\home\OneDrive\Documents\py\project.xlsx', sheet_name='Sheet_name_1')
    
