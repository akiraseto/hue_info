# hue_info
朝起きたとき、電球色で情報GET！Philips Hueの電球色でお知らせシステム

## 構成
ライトは6つ
− 天気（降水確率:晴れ、曇、雨）
− 気温（昨日と比較）
− 電車遅延してるか
- 運動量（withingsのstep数で昨日と一昨日の比較）
- 体重（昨日と一昨日の比較）
− 株（昨日と一昨日の比較）

### 体重を取得
- action: getmeas
- meastype: 体重の場合は1
- category: 今回は1
- startdate: 取得範囲 timestamp
- enddate: 取得範囲 timestamp

