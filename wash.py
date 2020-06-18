import pandas as pd
import jieba
from pandas import DataFrame,Series
import numpy as np
from word_dict import cov_dic

cov_dic = ['新冠','病毒','发烧']
set_cov_dic = set(cov_dic)
num_of_cov_webo = []
num_of_normal_webo = []
TRAIN_PATH = './data/train_dataset/'
NEW_FILE_cov = 'cov_data.csv'
NEW_FILE_nor = 'nor_data.csv'

df_train = pd.read_csv(TRAIN_PATH+'nCoV_100k_train.labled.csv',engine ='python')
df_train = df_train[df_train['情感倾向'].isin(['-1','0','1'])]
df_train['情感倾向'] = df_train['情感倾向'].astype(np.int32)

for i in range(10000):
  temp_ci = jieba.lcut(df_train['微博中文内容'][i])
  temp_ci = []
  set_temp_ci = set(temp_ci)
  if set_temp_ci & set_cov_dic:
    num_of_cov_webo.append(i)
  else:
    num_of_normal_webo.append(i)

def save_to_csv(list_name, csv_name):
  for i in list_name:
    data = {"微博id":[],
          "微博发布时间":[],
          "发布人账号":[],
          "微博中文内容":[],
          "微博图片":[],
          "微博视频":[],
          "情感倾向":[]
          }
    data['微博id'].append(df_train['微博id'][i])
    data['微博发布时间'].append(df_train['微博发布时间'][i])
    data['发布人账号'].append(df_train['发布人账号'][i])
    data['微博中文内容'].append(df_train['微博中文内容'][i])
    data['微博图片'].append(df_train['微博图片'][i])
    data['微博视频'].append(df_train['微博视频'][i])
    data['情感倾向'].append(df_train['情感倾向'][i])
    res=DataFrame(data, 
                  columns=["微博id","微博发布时间","发布人账号",
                          "微博中文内容","微博图片","微博视频","情感倾向"])
    res.to_csv(TRAIN_PATH + csv_name, header=False, index=False)

