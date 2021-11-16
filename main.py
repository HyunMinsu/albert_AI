import pandas as pd
from flask import Flask, request, json
import random
import os

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}
}


df = pd.read_csv("bbanglist.csv", encoding='cp949')
list_df = df.values.tolist()
num=0
# for data in list_df:
#     bbang_shop_name = list_df[num][0]
#     bbang_shop_best = list_df[num][1]
#     bbang_shop_time = list_df[num][2]
#     bbang_shop_address = list_df[num][3]
#     num = num + 1

for data in list_df:
    print(list_df[num][0])
    print(list_df[num][1])
    print(list_df[num][2])
    print(list_df[num][3])
    num = num + 1


@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/getlistofshop', methods=['POST'])
def getshoplist():
    response = commonResponse

    response['output']['bbang_shop_name'] = bbang_shop_name
    response['output']['bbang_shop_time'] = bbang_shop_best
    response['output']['bbang_shop_best'] = bbang_shop_time
    response['output']['bbang_shop_address'] = bbang_shop_address
    print(response)
    return json.dumps(response)

# print(bbang_shop_name)
# print(bbang_shop_address)
# print(bbang_shop_time)
# print(bbang_shop_best)
