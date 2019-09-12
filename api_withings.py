import requests
import json
import withings_token_refresh
import datetime

#GETで変数をpayloadして取得する

class Withings():
    def __init__(self):
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
        self.uni_yesterday = yesterday.strftime('%s') #分割用
        uni_before_yesterday = before_yesterday.strftime('%s')

        # y-m-d
        str_yesterday = yesterday.strftime('%Y-%m-%d')
        self.str_before_yesterday = before_yesterday.strftime('%Y-%m-%d')

        #体重
        self.WEIGHT_FILE_NAME = "tmp/weight.json"
        self.WEIGHT_URL = "https://wbsapi.withings.net/measure"
        self.WEIGHT_PARAMS ={
            'action': 'getmeas',
            'access_token': access_token,
            'meastype': 1,
            'category': 1,
            'startdate': uni_before_yesterday,
            'enddate': uni_today
        }

        #step数
        self.STEP_FILE_NAME = "tmp/step.json"
        self.STEP_URL = "https://wbsapi.withings.net/v2/measure"
        self.STEP_PARAMS ={
            'action': 'getactivity',
            'access_token': access_token,
            'offset': 0,
            'data_fields': 'steps',
            'startdateymd': self.str_before_yesterday,
            'enddateymd': str_yesterday
        }


    def weight_download(self):
        results = requests.get(self.WEIGHT_URL, self.WEIGHT_PARAMS)
        results = results.json()
        fw = open(self.WEIGHT_FILE_NAME,'w')
        json.dump(results,fw,indent=4)
        return results

    def step_download(self):
        results = requests.get(self.STEP_URL, self.STEP_PARAMS)
        results = results.json()
        fw = open(self.STEP_FILE_NAME,'w')
        json.dump(results,fw,indent=4)
        return results

    def get_weight(self):
        before_yester_list = []
        yester_list = []
        with open('tmp/weight.json', 'r') as f:
            JSONData = json.load(f)

        for i in JSONData['body']['measuregrps']:
            if int(self.uni_yesterday) > i['date']:
                before_yester_list.append(i['measures'][0]['value'])
            else:
                yester_list.append(i['measures'][0]['value'])

        mean_before_yester = round(sum(before_yester_list) / len(before_yester_list))
        mean_yester = round(sum(yester_list) / len(yester_list))

        return mean_before_yester, mean_yester

    def get_steps(self):
        steps_before = 0
        steps_yester = 0
        with open('tmp/step.json', 'r') as f:
            JSONData = json.load(f)

        for i in JSONData['body']['activities']:
            if self.str_before_yesterday == i['date']:
                steps_before = i['steps']
            else:
                steps_yester = i['steps']

        return steps_before, steps_yester

