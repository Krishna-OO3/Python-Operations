from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("2021-08-17commerce_event-443804504849141782.csv")

# 1-To view Single countries purchase data (user_data_geo_country_code){You can give any countries values to seperately view that countries datas}
# 2-Must not include unpaid customers
#   i.e {the customers who have initiated purchase and never made a purchase inside the app} (name)

# df_IN = df[ df['user_data_geo_country_code'] == 'IN']
# df_IN['timestamp_iso'] = pd.to_datetime( df_IN['timestamp_iso'])

# df_INSpent = df_IN[ df_IN['name'] == 'SPEND_CREDITS']

# 3-Avoid all the columns except amount that is the revenue got form the all country for that day {In common amount calculated}
df_user = df[ df['origin'] == 'BRANCH']
df_user = df_user[ df_user['name'] == 'SPEND_CREDITS']
# series_user_spent_sum = df_user.groupby('name')['event_data_revenue_in_usd'].sum()

plt.plot()
