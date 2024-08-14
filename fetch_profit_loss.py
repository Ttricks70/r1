import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load credentials
with open("credentials/credentials.txt", "r") as f:
    creds = dict(line.strip().split('=') for line in f)

# Log into Screener.in
session = requests.Session()
login_payload = {
    'username': creds['username'],
    'password': creds['password'],
}
login_url = 'https://www.screener.in/login/'
session.post(login_url, data=login_payload)

# Fetch data from Screener.in
url = 'https://www.screener.in/company/RELIANCE/consolidated/'
response = session.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract profit and loss data (adjust based on actual HTML structure)
table = soup.find('table')  # Example, adjust as needed
df = pd.read_html(str(table))[0]

# Save to Excel
df.to_excel('data/profit_loss_data.xlsx', index=False)
