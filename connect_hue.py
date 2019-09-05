from phue import Bridge
import config

# huebridgeのIPアドレス 固定にしておく
b = Bridge(config.huebridge_ip)

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# Turn lamp 1 on
b.set_light(1,'on', True)

# todo:apiで天気予報を取得して表示
