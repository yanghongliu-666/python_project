from word_dict import posi_dict,nati_dict,fuci_dict_1,fuci_dict_2,nodict,fanwendict
import math
#判断中性词
def decide_neu(cut_list):
  pl_ans = posi_left_nagative_right(cut_list)
  pr_ans = posi_right_nagative_left(cut_list)
  if pl_ans and not pr_ans:
    return 0
  elif not pl_ans and pr_ans:
    return 0
  else:
    return 404

#积极在左，消极在右
def posi_left_nagative_right(cut_list):
  position_of_positive = 0
  position_of_nagative = 0
  num = len(cut_list)
  for i in range(num):
    if cut_list(i) in posi_dict:
      weight = check_before()
      if weight == 0:
        position_of_positive += i
      else:
        position_of_positive -= weight*i#特别正向左移
    elif cut_list(i) in nati_dict:
      weight = check.check_before()
      if weight == 0:
        position_of_nagative += i
      else:
        position_of_nagative += weight*i#特别负向右移
  
  if position_of_positive < position_of_nagative:
    return 1
  else:
    return 0

#积极在右，消极在左
def posi_right_nagative_left(cut_list):
  position_of_positive = 0
  position_of_nagative = 0
  num = len(cut_list)
  for i in range(num):
    if cut_list(i) in posi_dict:
      weight = check_before()
      if weight == 0:
        position_of_positive += i
      else:
        position_of_positive += weight*i#特别正向右移
    elif cut_list(i) in nati_dict:
      weight = check.check_before()
      if weight == 0:
        position_of_nagative += i
      else:
        position_of_nagative -= weight*i#特别负向左移
  
  if position_of_positive > position_of_nagative:
    return 1
  else:
    return 0
#判别副词、否定词、及相关位置
def check_before(cut_list, pos):
  numofno=0#否定词的数量
  numoffu = 0#副词的数量
  jioffu = 0#副词的极性
  placeofno = 0#否定词的位置
  placeoffu = 0#副词的位置
  allno = 0#否定词的综合作用
  tp =0#词性的综合作用
  for i in range(pos-5,pos):
    if cut_list[i] in nodict:
      numofno += 1
      if placeofno == 0:
        placeofno = i
    if cut_list[i] in fuci_dict_1:
      numoffu += 1
      jioffu = 3
      if placeoffu == 0:
        placeoffu = i
    if cut_list[i] in fuci_dict_2:
      numoffu += 1
      jioffu = 2.1
      if placeoffu == 0:
        placeoffu = i
  if numofno == 0:
    allno = 1
  else:
    allno = math.pow(-1,numofno)
  
  if placeoffu < placeofno:
    tp = -2
  if placeoffu > placeofno:
    tp = 0.5
  else:
    tp = 1
  return tp*allno*jioffu
  
#判别句型因素
def relation(cut_list):
  Hw = 0#感叹号的数量
  Yw = 0#问号的数量
  ci = 0#反问词的出现情况
  fi = 1#综合的句型因素
  for i in range(len(cut_list)):
    if'!'== cut_list[i]:
      Hw += 1
    if '?' == cut_list:
      Yw += 1
    if cut_list[i] in fanwendict:
      ci += 1
  if Hw == 0:
    fi *= 1
  if Hw == 1 or Hw == 2:
    fi*=2
  if Yw>0 and ci>0:
    fi *= -1
  return fi
  
  



 