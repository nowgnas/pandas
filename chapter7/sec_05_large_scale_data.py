import pandas as pd

from importFile import *

# with open('../doit_pandas/data/raw_data_urls.txt', 'r') as data_urls:
#     for line, url in enumerate(data_urls):
#         if line == 5:
#             break
#         fn = url.split('/')[-1].strip()
#         print(fn)
#         fp = os.path.join('', '../doit_pandas/data', fn)
#         print(url)
#         print(fp)
#         urllib.request.urlretrieve(url, fp)

nyc_taxi_data = glob.glob('../doit_pandas/data/fhv_*')
print(nyc_taxi_data)

taxi1 = pd.read_csv(nyc_taxi_data[0])
taxi2 = pd.read_csv(nyc_taxi_data[1])
taxi3 = pd.read_csv(nyc_taxi_data[2])
taxi4 = pd.read_csv(nyc_taxi_data[3])
taxi5 = pd.read_csv(nyc_taxi_data[4])

# print(taxi5.head())

# 데이터프레임 연결하기
taxi = pd.concat([taxi1, taxi2, taxi3, taxi4, taxi5])
print(taxi.shape)

