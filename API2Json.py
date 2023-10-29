#!python3.10
# import json
import streamlit as st
import requests
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import os

st.title("外部APIをスプレッドシートに反映する")
st.caption("下部にURLをスプシKeyを入力")
submit_btn = st.button("送信")
cancel_btn = st.button("キャンセル")


JsonURL = st.text_input("API URL")
GSkey = st.text_input("スプレッドシートのKey")
loc = JsonURL
header = {"content-type": "application/json"}
r = requests.get(loc, headers=header)
df = pd.read_json(loc)
st.text(df)

dir_path = os.path.dirname(__file__) # 作業フォルダの取得
gc = gspread.oauth(
                   credentials_filename=os.path.join(dir_path, "client_secret_1011947998521-u1oqvpcfifmbk68red1h2pu6njcjrvro.apps.googleusercontent.com.json"), # 認証用のJSONファイル
                   authorized_user_filename=os.path.join(dir_path, "C:/Users/I-zy/PycharmProjects/Gsheets/authorized_user.json"), # 証明書の出力ファイル
                   )

# スプレッドシートに書き込み
wb = gc.open_by_key(GSkey) # test02のファイルを開く(キーから)
ws = wb.get_worksheet(0) # 最初のシートを開く(idは0始まりの整数)

data = df
set_with_dataframe(ws,data.reset_index())
# 複数行一括書き込み
# wb.values_append("シート1", {"valueInputOption": "USER_ENTERED"}, {"values": data})