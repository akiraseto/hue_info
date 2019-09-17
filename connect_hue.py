from phue import Bridge
import config

import api_weather
import api_train
import api_withings
import api_stock

import sys

# 昼光色(6500K)
daylight = {'on' : True,  "bri": 255, "ct": 153}
# 赤
red = {'on' : True,  "bri": 255, "hue": 65535, "sat": 255}
# 青
blue = {'on' : True,  "bri": 255, "hue": 46000, "sat": 255}
# 緑
green = {'on' : True,  "bri": 255, "hue": 25000, "sat": 255}
# 黄
yellow = {'on' : True,  "bri": 255, "hue": 9500, "sat": 255}


weather = api_weather.Weather()
weather.download()
# '晴のち曇'と、 ['20', '20']でリターン
res_weather, res_temp = weather.get_weather()

# 天気 雨があるなら0,曇があるなら1,晴のみなら2
chk_weather = None
if '雨' in res_weather:
    chk_weather = blue
elif '曇' in res_weather:
    chk_weather = green
elif '晴' in res_weather:
    chk_weather = yellow
else:
    chk_weather = daylight

# 気温の比較
chk_temp = None
if res_temp[0] < res_temp[1]:
    chk_temp = red
elif res_temp[0] == res_temp[1]:
    chk_temp = green
else:
    chk_temp = blue


train = api_train.Train()
train.download()
# (2, '鹿島線 呉線 ') でリターン
res_train = train.get_delay_train()

# 電車 遅延の本数
chk_train = None
if res_train[0] == 2:
    chk_train = red
elif res_train[0] == 1:
    chk_train = yellow
else:
    chk_train = blue


stock = api_stock.Stock()
stock.download()
# (2, [21318, 21392]) でリターン
res_stock = stock.get_stock()

# 株価の比較
chk_stock = None
if res_stock[1][0] < res_stock[1][1]:
    chk_stock = blue
elif res_stock[1][0] == res_stock[1][1]:
    chk_stock = green
else:
    chk_stock = red


withings = api_withings.Withings()
withings.weight_download()
withings.step_download()

# (65700, 66000) でリターン
res_weight = withings.get_weight()
# (10548, 14260) でリターン
res_steps = withings.get_steps()

# withings 体重の比較
chk_weight = None
if res_weight[0] < res_weight[1]:
    chk_weight = red
elif res_weight[0] == res_weight[1]:
    chk_weight = green
else:
    chk_weight = blue

# withings step数の比較
chk_steps = None
if res_steps[0] < res_steps[1]:
    chk_steps = blue
elif res_steps[0] == res_steps[1]:
    chk_steps = green
else:
    chk_steps = red

# huebridgeのIPアドレス 固定にしておく
b = Bridge(config.huebridge_ip)

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# 照明1番:ambient:昼光色
b.set_light(10, daylight, True)
# 照明2番:color:天気
b.set_light(1, chk_weather, True)
# 照明3番:color:気温
b.set_light(2, chk_temp, True)
# 照明4番:color:電車
b.set_light(3, chk_train, True)
# 照明8番:color: 株
b.set_light(8, chk_stock, True)
# 照明10番:color:体重
b.set_light(7, chk_weight, True)
# 照明9番:color:STEP数
b.set_light(6, chk_steps, True)

for i in 4,5,9:
    b.set_light(i,'on', False)



sys.exit()
