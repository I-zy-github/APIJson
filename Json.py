import requests
import gspread
import os

loc = "https://sheets.googleapis.com/v4/spreadsheets/1-6NL6sZIC4XcbwE7BsZYLBBoeByvZNeqhyFKm15X6ls/values/Monolith?key=AIzaSyBBY5QhOXZfkTp_Y8828C00ad7Gf6NTdgQ"
header = {"content-type": "application/json"}
r = requests.get(loc, headers=header)
print(r.json())



dir_path = os.path.dirname(__file__) # 作業フォルダの取得
gc = gspread.oauth(
                   credentials_filename=os.path.join(dir_path, "client_secret.json"), # 認証用のJSONファイル
                   authorized_user_filename=os.path.join(dir_path, "authorized_user.json"), # 証明書の出力ファイル
                   )

wb = gc.create("test01") # スプレッドシート作成