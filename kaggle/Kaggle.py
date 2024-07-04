import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import pandas as pd

# Create the data directory if it doesn't exist
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Set up Selenium webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.kaggle.com/datasets?tags=12107-Computer+Science"

# Open the URL using Selenium
driver.get(url)

# Wait for the page to load and dynamically render content (adjust the timeout as needed)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiListItem-root.MuiListItem-gutters.MuiListItem-divider.sc-guhxjM.kLylVR.css-iicyhe")))

# Get the updated page source after content has loaded
html = driver.page_source

# Close the webdriver
driver.quit()

# Parse the HTML using BeautifulSoup
soup = bs(html, "html.parser")

# Find the dataset containers using the correct class name
containers = soup.find_all("li", {"class": "MuiListItem-root MuiListItem-gutters MuiListItem-divider sc-guhxjM kLylVR css-iicyhe"})

# Check the number of containers found
print(f"Number of containers found: {len(containers)}")

# Save CSV file to the user's home directory
csv_file_path = os.path.join(os.path.expanduser('~'), "Kaggle.csv")

with open(csv_file_path, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Dataset_title", "Creator", "Dataset_link"])

    for container in containers:
        Dataset_title_element = container.find("div", {"class": "sc-blmEgr sc-fGrmBj iVVdBa doCOYX"})
        Dataset_title = Dataset_title_element.text.strip() if Dataset_title_element else "N/A"
        
        Creator_element = container.find("a", {"class": "sc-eAKtBH gfxjtA"})
        Creator = Creator_element.text.strip() if Creator_element else "N/A"
        
        link_element = container.find("a", {"class": "sc-bqOYya camFgS"})
        Dataset_link = "https://www.kaggle.com" + link_element['href'] if link_element else "N/A"
        
        writer.writerow([Dataset_title, Creator, Dataset_link])

df = pd.read_csv(csv_file_path)
print(df)
