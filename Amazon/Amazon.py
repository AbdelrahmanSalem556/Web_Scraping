import os
import csv
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# Create the data directory if it doesn't exist
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

url = "https://www.amazon.eg/s?k=ipone+xs&crid=21ZHWB5HJNNOB&sprefix=ipone+x%2Caps%2C192&ref=nb_sb_ss_ts-doa-p_3_7"
mobile = urlopen(url)
html = mobile.read()
mobile.close()

soup = bs(html, "html.parser")
containers = soup.find_all("div", {"class": "a-section a-spacing-base"})

csv_file_path = os.path.join(data_dir, "iPhone_Info.csv")

with open(csv_file_path, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Model", "Price (EGP)", "Rating"])

    for container in containers:
        mobile_name_elements = container.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
        mobile_name = mobile_name_elements[0].text.strip() if mobile_name_elements else "N/A"

        mobile_price_elements = container.find_all("span", {"class": "a-price-whole"})
        mobile_price = mobile_price_elements[0].text.strip() if mobile_price_elements else "N/A"

        mobile_rate_elements = container.find_all("span", {"class": "a-icon-alt"})
        mobile_rate = mobile_rate_elements[0].text.strip() if mobile_rate_elements else "N/A"

        writer.writerow([mobile_name, mobile_price, mobile_rate])

print("CSV file created successfully!")
