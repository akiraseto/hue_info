# hue_info
朝起きたとき、電球色で情報GET！Philips Hueの電球色でお知らせシステム

![livingroom](https://user-images.githubusercontent.com/18400866/67646808-162b4300-f973-11e9-879e-2b3966d0b026.jpeg)

## 構成
ライトは6つ
- 天気（降水確率:晴れ、曇、雨）
    - api_weather
    - 雨の一文字あるなら:青
    - 曇の一文字あるなら:緑
    - 晴の一文字あるなら:黄

- 気温（昨日と比較）
    - api_weather
    - 昨日 < 今日:赤
    - 昨日 = 今日:緑
    - 昨日 > 今日:青

- 電車遅延してるか
    - api_train
    - 2本遅延している:赤
    - 1本遅延している:黄
    - 遅延無し:青

- 運動量（withingsのstep数で昨日と一昨日の比較）
    - api_withings
    - 一昨日 < 昨日:青
    - 一昨日 = 昨日:緑
    - 一昨日 > 昨日:赤

- 体重（昨日と一昨日の比較）
    - api_withings
    - 一昨日 < 昨日:赤
    - 一昨日 = 昨日:緑
    - 一昨日 > 昨日:青
    
    
- 株（昨日と一昨日の比較）
    - api_stock
    - 一昨日 < 昨日:青
    - 一昨日 = 昨日:緑
    - 一昨日 > 昨日:赤

### 照明色設定
- 赤:"hue": 65535
- 青:"hue": 46000
- 緑:"hue": 25000
- 黄:"hue": 9500

同一パラメーター: "bri": 255, "sat": 255
昼光色:"ct": 153

## Hue情報

- brightness : level = (int)        - int is from 0 to 255  
- hue        : level = ('hue:int')  - int is from 0 to 65535
- saturation : level = ('sat:int')  - int is from 0 to 255  
- ct         : level = ('ct:int')   - int is from 153 to 500  
     153 to 500 == 6500K to 2000K  
     昼光色6500K(153)一番白い  
- rgb        : level = ('rgb:hex')  - hex is from 000000 to ffffff
- transition : level = ('tr:int')   - int is from 0 to 3000 in tenths of seconds
- effect     : level = ('eft:colorloop|none') put bulb in colour loop

### デフォルト
- color lamp : b:254,h:8418,s:140,(ct:366)
- ambiance lamp : b:254,ct:366


## 体重を取得
- action: getmeas
- meastype: 体重の場合は1
- category: 今回は1
- startdate: 取得範囲 timestamp
- enddate: 取得範囲 timestamp

