from word_dict import posi_dict,nati_dict,fuci_dict_1,fuci_dict_2

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

def check_before(cut_list, pos):
  if cut_list[pos-1] in fuci_dict_1:
    return 4#要改
  elif cut_list[pos-1] in fuci_dict_2:
    return 8#要改
  else:
    return 0#default
