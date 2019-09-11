from phue import Bridge
import config

import api_weather
import api_train
# import api_withings
import api_stock

import sys

weather = api_weather.Weather()
weather.download()
# 「晴れのち曇り」でリターン
res_weather = weather.get_weather()
# todo:気温も取る、忘れてた。

train = api_train.Train()
train.download()
# (2, '鹿島線 呉線 ') でリターン
res_train = train.get_delay_train()

stock = api_stock.Stock()
stock.download()
# (2, [21318, 21392]) でリターン
res_stock = stock.get_stock()



print(res_stock)
sys.exit()

# huebridgeのIPアドレス 固定にしておく
b = Bridge(config.huebridge_ip)

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# Turn lamp 1 on
b.set_light(1,'on', True)

