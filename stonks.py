import requests
import pandas as pd
from io import BytesIO



url_path = "https://www.ice.com/publicdocs/clear_europe/irmParameters/harmonized/ENERGY_MARGIN_SCANNING_20240115.CSV"
resp = requests.get(url_path)
by = resp.content
df = pd.read_csv(BytesIO(by))
print(df.head())
df.to_csv("/Users/patrick/Desktop/stonks/willitwork.csv")
