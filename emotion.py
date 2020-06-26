import pandas as pd
import jieba
import function as fun
from pandas import DataFrame,Series
from word_dict import posi_dict,nati_dict

#对于疫情相关的微博的情感分析
TRAIN_PATH = './data/train_dataset/'
df_train = pd.read_csv(TRAIN_PATH+'nCoV_100k_train.labled.csv',engine ='python')

for i in range(10000):
  all_emotion_num = 0
  posi_emotion_num = 0
  nati_emotion_num = 0
  temp_ci = jieba.lcut(df_train['微博中文内容'][i])
  ju = fun.relation(temp_ci)
  for j in range(len(temp_ci)):
    if temp_ci[j] in posi_dict:
      weight = check_before()#检查副词
      if weight == 0:
        posi_emotion_num += 1
      else:
        posi_emotion_num += weight
    if temp_ci[j] in nati_dict:
      weight = check_before()
      if weight == 0:
        nati_emotion_num += 1
      else:
        nati_emotion_num += weight
  posi_emotion_num *= ju
  nati_emotion_num *= ju
  if posi_emotion_num > 0 and nati_emotion_num == 0:
    all_emotion_num = 1
  
  elif nati_emotion_num > 0 and posi_emotion_num == 0:
    all_emotion_num = -1
  
  elif posi_emotion_num - 2 > nati_emotion_num:
    all_emotion_num = 1

  elif nati_emotion_num - 2 > posi_emotion_num:
    all_emotion_num = -1
  
  else:
    if fun.decide_neu(temp_ci) == 0:
      all_emotion = fun.decide_neu(temp_ci)#处理中性文本
    elif fun.decide_neu(temp_ci) == 404:
      if posi_emotion_num > nati_emotion_num:
        all_emotion = 1
      else:
        all_emotion = -1
    


