import urllib.request
import json

WEB_SERVICE_URL = "https://tetsudo.rti-giken.jp/free/delay.json"
SAVE_FILE_NAME = "tmp/delay.json"

#副都心線、田園都市線を検索
SEARCH_DATA_LABEL = ['田園都市線','副都心線']

def download():
    urllib.request.urlretrieve(WEB_SERVICE_URL, SAVE_FILE_NAME)

def get_delay_train(data_label):
    delay = []
    with open(SAVE_FILE_NAME, 'r') as f:
        JSONData = json.load(f)
        for i in range(len(JSONData)):
            for j in range(len(data_label)):
                if JSONData[i]['name']  == data_label[j]:
                        delay.append(JSONData[i]['name'])
        return delay

if __name__ == "__main__":
    download()
    train = get_delay_train(SEARCH_DATA_LABEL)
    text = ''
    for i in range(len(train)):
        text += train[i]
        text += ' '

    print('遅延の本数は' + str(len(train)) + '件です')
    print('遅延路線は' + text + 'です')

