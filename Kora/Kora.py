import os
import requests
import csv
from bs4 import BeautifulSoup as bs

# Create the data directory if it doesn't exist
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

url = "https://www.filgoal.com/matches/?date=2024-04-18"

response = requests.get(url)
soup = bs(response.content, "html.parser")

containers = soup.findAll("div", {"class": "mc-block"})

csv_file_path = os.path.join(data_dir, "kora.csv")

with open(csv_file_path, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Teams", "Match Details"])

    for container in containers:
        Teams = container.find("div", {"class": "c-i-next"}).text.strip()
        Match_stadium = container.find("div", {"class": "match-aux"}).text.strip()

        writer.writerow([Teams, Match_stadium])

print("CSV file created successfully!")