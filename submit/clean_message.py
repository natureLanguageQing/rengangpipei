import pandas as pd

submit_message: pd.DataFrame = pd.read_csv("zhaopin_round1_submit_20190716 (1).csv")
print(submit_message.count())
df3 = submit_message.drop_duplicates(['user_id'])
print(df3.count())