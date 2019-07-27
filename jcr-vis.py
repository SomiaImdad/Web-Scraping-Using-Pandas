import pandas as pd

import requests

from datetime import date

url = 'http://jcrvis.com.pk/ratingSect.aspx?sec=29'

html = requests.get(url).content

df_list = pd.read_html(html, flavor='bs4', header=1)

for i in range(0, len(df_list)):
    df = df_list[i]

    print(df.head(100))
