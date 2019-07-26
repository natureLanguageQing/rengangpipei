# f = open("table1_user", "r", encoding='utf-8')
# fil = []
# for i in f.readlines():
#     if i not in fil:
#         fil.append(i)
# print('人数', len(fil))
#
# jd = open('table2_jd', "r", encoding='utf-8')
# j = []
# print('未去重岗位数', len(jd.readlines()))
#
# action = open('table3_action', encoding='utf-8')
# print('人岗匹配数量', len(action.readlines()))

import pandas as pd

table_user = pd.read_csv('table1_user', sep="\t")
print(table_user.count())

table_user = pd.read_csv('table2_jd', sep="\t")
print(table_user.count())

table_user = pd.read_csv('table3_action', sep="\t")
print(table_user.count())
