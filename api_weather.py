import urllib.request
import json
import os

class Weather():

    def __init__(self):
        self.WEB_SERVICE_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
        self.CITY_ID = 130010
        self.SAVE_FILE_NAME = "tmp/weather.json"
        self.OLD_FILE_NAME = "tmp/old_weather.json"

        #今日、明日、明後日を設定
        self.SEARCH_DATA_LABEL = '今日'

    def download(self):
        if os.path.exists(self.SAVE_FILE_NAME):
            os.rename(self.SAVE_FILE_NAME, self.OLD_FILE_NAME)

        open_url = self.WEB_SERVICE_URL + str(self.CITY_ID)
        urllib.request.urlretrieve(open_url, self.SAVE_FILE_NAME)

    def get_weather(self):
        weather = ''
        temp = []

        # 昨日の気温だけを取得
        with open(self.OLD_FILE_NAME, 'r') as f:
            JSONData = json.load(f)
            forecasts_list = JSONData['forecasts']
            for i in range(len(forecasts_list)):
                if forecasts_list[i]['dateLabel']  == self.SEARCH_DATA_LABEL:
                    temp.append(forecasts_list[i]['temperature']['max']['celsius'])
                break

        # 今日の天気と、気温を取得
        with open(self.SAVE_FILE_NAME, 'r') as f:
            JSONData = json.load(f)
            forecasts_list = JSONData['forecasts']
            for i in range(len(forecasts_list)):
                if forecasts_list[i]['dateLabel']  == self.SEARCH_DATA_LABEL:
                    weather = forecasts_list[i]['telop']
                    temp.append(forecasts_list[i]['temperature']['max']['celsius'])
                break

        return weather, temp
