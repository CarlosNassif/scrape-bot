# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:26:28 2022

@author: Carlos
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# need to add headers
def review_count_scrape():
    url = "https://coronavirus.saude.mg.gov.br/boletim"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0", 
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3'
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    # print(soup)
        
    fileHref = [i.text + ":" + i['href'] for i in soup.findAll('a', class_='wf_file')]
    df = pd.DataFrame(fileHref)
    filename = str(time.time())
    df.to_csv(filename + '- file urls.csv')
    
    print(df)
    
    time.sleep(60)
    
end_timer = time.time() + 60 * 2
while time.time() < end_timer:
    review_count_scrape()
