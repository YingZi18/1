#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：王英子
日期：2020.4.9
"""

import random
print("欢迎使用RPSLS游戏")
print("请输入您的选择:")
choice_name=input()
print("----------------")
def name_to_number(choice_name): #将选择对象转换为数字
 if choice_name=="剪刀":
  return 4
 elif choice_name=="石头":
  return choice_name==0
 elif choice_name=="史波克":
   return 1
 elif choice_name=="纸":
   return 2
 elif choice_name=="蜥蜴":
  return 3
 else: 
  return "Error: No Correct Name"
	  
player_choice_number=name_to_number(choice_name)
print("您的选择为"+choice_name)

comp_number=int(random.randint(0,5) )#随机产生0,1,2,3,4

def number_to_name(comp_number):#将计算机的数字转换为对象
 if comp_number==0:
   return "石头"
 elif comp_number==1:
   return "史波克"
 elif comp_number==2:
   return "纸"
 elif comp_number==3:
   return "蜥蜴"
 elif comp_number==4:
   return "剪刀"
print("计算机的选择是"+str(number_to_name(comp_number)))

def rpsls(player_choice_number,comp_number):#根据规则判断输赢
 if (player_choice_number==comp_number):
    return"您和计算机出的一样呢"
 elif (player_choice_number==2 and (comp_number==1 or 0)) or (player_choice_number==3 and (comp_number==1 or 2)):
      return "您赢了!"
 elif (player_choice_number==0 and (comp_number==3 or 4)) or (player_choice_number==1 and (comp_number==4 or 0)) or (player_choice_number==4 and (comp_number==2 or 3)) :  
    return "您赢了!"
 elif (comp_number==2 and (player_choice_number==1 or 0)) or (comp_number==3 and (player_choice_number==1 or 2)):
   return "计算机赢了"
 elif (comp_number==0 and (player_choice_number==3 or 4)) or (comp_number==1 and (player_choice_number==4 or 0)) or (comp_number==4 and (player_choice_number==2 or 3)):
	 return "计算机赢了"
 else:
	 return "Error: No Correct Name" 

print (rpsls(player_choice_number,comp_number))#输出结果





