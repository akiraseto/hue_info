import urllib.request
import json
import os
import glob
import datetime

class Weather():

    def __init__(self):
        # todo:livedoorだと気温が時々失敗する、OpenWeatherMapを検討？
        self.WEB_SERVICE_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
        self.CITY_ID = 130010
        self.SAVE_FILE_NAME = "tmp/weather.json"

        yesterday = datetime.date.today() - datetime.timedelta(1)
        str_yesterday = yesterday.strftime('%Y-%m-%d')
        self.old_file_name = "tmp/" + str_yesterday + "_weather.json"

        #今日、明日、明後日を設定
        self.SEARCH_DATA_LABEL = '今日'

    def download(self):
        # 日付付きのフィル名に変更する
        if os.path.exists(self.SAVE_FILE_NAME):
            #日付取得
            with open(self.SAVE_FILE_NAME, 'r') as f:
                JSONData = json.load(f)
                forecasts_list = JSONData['forecasts']
                for i in range(len(forecasts_list)):
                    if forecasts_list[i]['dateLabel']  == self.SEARCH_DATA_LABEL:
                        date = forecasts_list[i]['date']
                    break

            # 日付付きの古いファイルを削除
            file_list = sorted(glob.glob('tmp/*_weather.json'))
            for i in file_list:
                os.remove(i)
            #日付を付けてリネーム
            self.old_file_name = "tmp/" + date + "_weather.json"
            os.rename(self.SAVE_FILE_NAME, self.old_file_name)

        # 新規のファイルを取得
        open_url = self.WEB_SERVICE_URL + str(self.CITY_ID)
        urllib.request.urlretrieve(open_url, self.SAVE_FILE_NAME)

    def get_weather(self):
        weather = ''
        temp = []

        # 昨日の気温だけを取得
        with open(self.old_file_name, 'r') as f:
            JSONData = json.load(f)
            forecasts_list = JSONData['forecasts']
            for i in range(len(forecasts_list)):
                if forecasts_list[i]['dateLabel']  == self.SEARCH_DATA_LABEL:
                    try:
                        temp.append(int(forecasts_list[i]['temperature']['max']['celsius']))
                    except Exception as e:
                        temp.append(20)
                        print('昨日: ',e)
                break

        # 今日の天気と、気温を取得
        with open(self.SAVE_FILE_NAME, 'r') as f:
            JSONData = json.load(f)
            forecasts_list = JSONData['forecasts']
            for i in range(len(forecasts_list)):
                if forecasts_list[i]['dateLabel']  == self.SEARCH_DATA_LABEL:
                    weather = forecasts_list[i]['telop']
                    try:
                        temp.append(int(forecasts_list[i]['temperature']['max']['celsius']))
                    except Exception as e:
                        temp.append(20)
                        print('今日: ',e)
                break

        return weather, temp
