import requests
import pandas as pd
from io import BytesIO
import time




today = time.strftime("%Y-%m-%d")
date_value = today.replace('-', '')
print(date_value)


# Working URL
url_path = "https://www.ice.com/publicdocs/clear_europe/irmParameters/harmonized/ENERGY_MARGIN_SCANNING_20240115.CSV"

url_for_reuse = f"https://www.ice.com/publicdocs/clear_europe/irmParameters/harmonized/ENERGY_MARGIN_SCANNING_{date_value}.CSV"

resp = requests.get(url_path)
by = resp.content
df = pd.read_csv(BytesIO(by))
print(df.head())
date_value = 1
df.to_csv(f"/Users/patrick/Desktop/stonks/{date_value}-report.csv")
