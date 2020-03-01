import requests
# import pandas as pd
# from datetime import datetime
import time

import os
os.chdir('/Users/kevink/projects/surf_forecast/surf_app')

import config_msw

spots = [382,2159]

# pull data from MSW
sitedata=requests.get("http://magicseaweed.com/api/" + config_msw.msw["key"] + "/forecast/?spot_id=" + str(spots[1]))

print(sitedata.status_code)
# print(sitedata.json())

# type(sitedata.json()[0])
# len(sitedata.json())

# df = pd.DataFrame.from_dict(sitedata.json()[0])
# df.head()

# save data somewhere
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")

outfile = open("data.txt", "a") # "a" flag will append lines

outfile.write(str(int(time.time())) + ":" + str(sitedata.status_code) + "\n")

outfile.close()
