import urllib.request
import json

class Train():
    def __init__(self):
        self.WEB_SERVICE_URL = "https://tetsudo.rti-giken.jp/free/delay.json"
        self.SAVE_FILE_NAME = "tmp/delay.json"

        #副都心線、田園都市線を検索
        # self.SEARCH_DATA_LABEL = ['田園都市線','副都心線']
        self.SEARCH_DATA_LABEL = ['鹿島線','呉線']

    def download(self):
        urllib.request.urlretrieve(self.WEB_SERVICE_URL, self.SAVE_FILE_NAME)

    def get_delay_train(self):
        delay = []
        delay_line = ''

        with open(self.SAVE_FILE_NAME, 'r') as f:
            JSONData = json.load(f)
            for i in range(len(JSONData)):
                for j in range(len(self.SEARCH_DATA_LABEL)):
                    if JSONData[i]['name']  == self.SEARCH_DATA_LABEL[j]:
                        delay.append(JSONData[i]['name'])

        delay_num = len(delay)
        for j in range(delay_num):
            delay_line += delay[j]
            delay_line += ' '

        return delay_num, delay_line

