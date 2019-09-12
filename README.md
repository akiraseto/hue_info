# hue_info
朝起きたとき、電球色で情報GET！Philips Hueの電球色でお知らせシステム

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

### 体重を取得
- action: getmeas
- meastype: 体重の場合は1
- category: 今回は1
- startdate: 取得範囲 timestamp
- enddate: 取得範囲 timestamp

