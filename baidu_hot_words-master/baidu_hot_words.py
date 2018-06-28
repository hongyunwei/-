
# coding: utf-8

# ## 百度新闻热搜词抓取

# In[1]:

import json
import requests  
from bs4 import BeautifulSoup


# In[2]:

# 基本Url
base_url = 'https://news.baidu.com/'  
hot_type = '0'

parameters = {'type': hot_type}

# 获取 JSON 数据
r = requests.get(base_url, params=parameters)  
newsdata=r.text
soup=BeautifulSoup(newsdata,'html.parser')
# 输出热搜关键词
for hotwords_li in soup.select('.hotwords_li_a'):
    print(hotwords_li.get_text())


