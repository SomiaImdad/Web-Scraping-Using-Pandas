import pandas as pd

import requests

from datetime import date
import urllib.request

html = urllib.request.urlopen('http://www.pacra.com.pk/reports/asset_management.php?1562871450315')

df_list = pd.read_html(html, flavor='bs4', header=0)

for i in range(0, len(df_list)):
    df = df_list[i][i]

    print(df.head(100))
