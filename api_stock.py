import datetime
import requests
import os
import glob
import zipfile
import pandas as pd

class Stock():
    def __init__(self):
        # 祝日apiを入手
        HOLIDAY_URL = "https://holidays-jp.github.io/api/v1/date.json"
        holiday_json = requests.get(HOLIDAY_URL)
        self.holiday_json = holiday_json.json()

        # 1月2,3日を追加する
        this_year = int(sorted(self.holiday_json.keys())[0][:4])
        add_holiday = {}
        for i in range(2):
            for j in range(2):
                add_holiday[str(this_year) + "-01-0{}".format(str(j++2))] = "正月休み"
            this_year += 1

        self.holiday_json.update(add_holiday)

        # 日付を用意
        today = datetime.date.today()
        self.yesterday = today - datetime.timedelta(1)
        self.str_yesterday = self.yesterday.strftime('%Y-%m-%d')

        # ファイルの操作場所
        self.target_directory = 'tmp/'

        self.csv_list =[]

    def download(self):
        # 昨日が土日や、祝日でないなら
        if self.yesterday.weekday() > 4 or self.str_yesterday in self.holiday_json:
            print("STOCK:営業外:DLできない")
        else:
            # 昨日のファイルをダウンロード
            year = self.yesterday.strftime('%Y')
            month = self.yesterday.strftime('%m')
            day = self.yesterday.strftime('%d')
            STOCK_URL = "http://souba-data.com/k_data/"
            STOCK_URL = STOCK_URL + year + "/" + year[2:] + "_" + month + "/T" + year[2:] + month + day + ".zip"
            dl_stock = requests.get(STOCK_URL, stream=True)

            # 成功ならZIPファイルを落として、解凍してCSVにする
            if dl_stock.status_code == 200:
                z_filename = "tmp/stock.zip"

                # zipファイルをダウンロード
                with open(z_filename, 'wb') as f:
                    for chunk in dl_stock.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()

                # zipを解凍してCSVを取得、リスト更新
                z_file = zipfile.ZipFile(z_filename)
                z_file.extractall(self.target_directory)

        # ダウンロード済みのcsvファイルリスト
        self.csv_list = sorted(glob.glob(self.target_directory + '*.csv'))

        # CSVが3つ以上あるなら、一番古いCSVファイル削除
        if len(self.csv_list) >= 3:
            print("STOCK:一番古いCSVを消す")

            day_name_list = []
            for i in self.csv_list:
                day_name_list.append(int(i[5:11]))
            min_num = str(min(day_name_list))

            _d_file = [s for s in self.csv_list if min_num in s]
            d_file = _d_file[0]

            if os.path.isfile(d_file) and len(self.csv_list) > 1:
                os.remove(d_file)
                # CSVリストを更新
                self.csv_list = sorted(glob.glob(self.target_directory + '*.csv'))

        elif len(self.csv_list) == 2:
                print("STOCK:ちょうどCSVが2つ")
        elif len(self.csv_list) == 1:
            print("STOCK:CSVが1つだけ")
        else:
            print("STOCK:エラー:CSVが無い、最初からDLして")

    def get_stock(self):
        # csvファイルをpandasに取り込み、株価比較
        prices = []

        if len(self.csv_list) == 1 :
            df1 = pd.read_csv(self.csv_list[0], encoding='cp932', header=None)
            prices.append(int(df1.loc[0][7]))

        elif len(self.csv_list) >= 2:
            df1 = pd.read_csv(self.csv_list[0], encoding='cp932', header=None)
            prices.append(int(df1.loc[0][7]))

            df2 = pd.read_csv(self.csv_list[1], encoding='cp932', header=None)
            prices.append(int(df2.loc[0][7]))
        else:
            print("STOCK:dataが無い")

        prices_num = len(prices)

        return prices_num, prices

