import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe



worksheet = [適宜シートを設定]

# sheetからdataframeで受け取る
df_sps = get_as_dataframe(worksheet, usecols=[0,1,2,3], skiprows=0, header=0, index_col=0)

#################
# ここでデータ処理
#################

# sheetに反映
set_with_dataframe(worksheet, df_sps.reset_index())