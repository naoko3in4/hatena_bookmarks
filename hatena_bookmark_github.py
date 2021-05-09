#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import slackweb

url = "https://b.hatena.ne.jp/"
slack_url = "" ## slackに通知するには slack incoming-webhook url を作成

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
unit = soup.find("section", attrs={"class": "entrylist-unit"})
boxes = unit.find_all("div", attrs={"class": "entrylist-contents"})

message = ""

for box in boxes:
    title_box = box.find("h3", attrs={"class": "entrylist-contents-title"})
    
    title = title_box.find("a").get("title")
    category = title_box.find("a").get("data-entry-category")
    content_href = title_box.find("a").get("href")
    
    user_num_box = box.find("span", attrs={"class": "entrylist-contents-users"})
    user_num = user_num_box.get_text().strip()

    
    message = message + format(user_num) + "/" + "《" + category + "》  \n" + title +"\n" + content_href+"\n"
print(message)

slack = slackweb.Slack(url=slack_url)
slack.notify(text=message)

