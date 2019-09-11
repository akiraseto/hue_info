import urllib.request
import json

class Weather():

    def __init__(self):
        self.WEB_SERVICE_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
        self.CITY_ID = 130010
        self.SAVE_FILE_NAME = "tmp/weather.json"

        #今日、明日、明後日を設定
        self.SEARCH_DATA_LABEL = '今日'

    def download(self):
        open_url = self.WEB_SERVICE_URL + str(self.CITY_ID)
        urllib.request.urlretrieve(open_url, self.SAVE_FILE_NAME)

    def get_weather(self):
        weather = ''
        with open(self.SAVE_FILE_NAME, 'r') as f:
            JSONData = json.load(f)
            forecasts_list = JSONData['forecasts']
            for i in range(len(forecasts_list)):
                if forecasts_list[i]['dateLabel']  == self.SEARCH_DATA_LABEL:
                    weather = forecasts_list[i]['telop']
                    break
            return weather
