import requests
import json
import withings_token_refresh
import datetime

#GETで変数をpayloadして取得する

#アクセストークン
#更新
wtr = withings_token_refresh.Token_refresh()
wtr.run()
#取得
with open('tmp/withings_token.json', 'r') as f:
    _access_token = json.load(f)
    access_token = _access_token['access_token']

# 日付
today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
before_yesterday = today - datetime.timedelta(2)

#unittime
uni_today = today.strftime('%s')
uni_yesterday = yesterday.strftime('%s') #分割用
uni_before_yesterday = before_yesterday.strftime('%s')

# y-m-d
str_yesterday = yesterday.strftime('%Y-%m-%d')
str_before_yesterday = before_yesterday.strftime('%Y-%m-%d')

#体重
WEIGHT_FILE_NAME = "tmp/weight.json"
WEIGHT_URL = "https://wbsapi.withings.net/measure"
WEIGHT_PARAMS ={
    'action': 'getmeas',
    'access_token': access_token,
    'meastype': 1,
    'category': 1,
    'startdate': uni_before_yesterday,
    'enddate': uni_today
}

#step数
STEP_FILE_NAME = "tmp/step.json"
STEP_URL = "https://wbsapi.withings.net/v2/measure"
STEP_PARAMS ={
    'action': 'getactivity',
    'access_token': access_token,
    'offset': 0,
    'data_fields': 'steps',
    'startdateymd': str_before_yesterday,
    'enddateymd': str_yesterday
}


def weight_download():
    results = requests.get(WEIGHT_URL, WEIGHT_PARAMS)
    results = results.json()
    fw = open(WEIGHT_FILE_NAME,'w')
    json.dump(results,fw,indent=4)
    return results

def step_download():
    results = requests.get(STEP_URL, STEP_PARAMS)
    results = results.json()
    fw = open(STEP_FILE_NAME,'w')
    json.dump(results,fw,indent=4)
    return results

def get_weight():
    before_yester_list = []
    yester_list = []
    with open('tmp/weight.json', 'r') as f:
        JSONData = json.load(f)

    for i in JSONData['body']['measuregrps']:
        if int(uni_yesterday) > i['date']:
            before_yester_list.append(i['measures'][0]['value'])
        else:
            yester_list.append(i['measures'][0]['value'])

    mean_before_yester = round(sum(before_yester_list) / len(before_yester_list))
    mean_yester = round(sum(yester_list) / len(yester_list))

    return mean_before_yester, mean_yester

def get_steps():
    steps_before = 0
    steps_yester = 0
    with open('tmp/step.json', 'r') as f:
        JSONData = json.load(f)

    for i in JSONData['body']['activities']:
        if str_before_yesterday == i['date']:
            steps_before = i['steps']
        else:
            steps_yester = i['steps']

    return steps_before, steps_yester


if __name__ == "__main__":
    weight = weight_download()
    step = step_download()

    print('weight')
    weight_before, weight_yester = get_weight()
    print(weight_before, weight_yester)

    print('step')
    steps_before, steps_yester = get_steps()
    print(steps_before, steps_yester)
