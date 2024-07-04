import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv
import pandas as pd

# Create the data directory if it doesn't exist
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

#date = input("Please enter the date: ")
url = f"https://wuzzuf.net/search/jobs/?a=navbg&q=illustrator&start"
clinet = urlopen(url)
html = clinet.read()
#print(html)
clinet.close()
soup = bs(html, "html.parser")
#print(soup)
containers = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
#print(len(containers))
# bs.prettify(containers[0])
job_title = containers[0].div.h2.text
#print(job_title)
company_name = containers[0].findAll("div", {"css-d7j1kk"})
#print(company_name[0].text)
job_type = containers[0].findAll("span", {"css-1ve4b75 eoyjyou0"})
#print(job_type[0].text)
csv_file_path = os.path.join(data_dir, "wuzzaf-illustrator.csv")
with open(csv_file_path, "w") as f:
    header = "job_title, company_name, job_type\n"
    f.write(header)

    for container in containers:
        job_title = container.div.h2.text
        company_name = container.findAll("div", {"css-d7j1kk"})
        company_name = company_name[0].text.strip()
        job_type = container.findAll("span", {"css-1ve4b75 eoyjyou0"})
        job_type = job_type[0].text.strip()
        #print( job_title )
        #print( company_name  )
        #print(  job_type )
        #print()
        #print(job_title + "," + company_name + "," + job_type )
        f.write(job_title + "," + company_name + "," + job_type + "\n")

print(pd.read_csv("D:\Yalla kora\data\wuzzaf-illustrator.csv"))
       