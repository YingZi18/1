#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���Ӣ��
���ڣ�2020.4.9
"""

import random
print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")
choice_name=input()
print("----------------")
def name_to_number(choice_name): #��ѡ�����ת��Ϊ����
 if choice_name=="����":
  return 4
 elif choice_name=="ʯͷ":
  return choice_name==0
 elif choice_name=="ʷ����":
   return 1
 elif choice_name=="ֽ":
   return 2
 elif choice_name=="����":
  return 3
 else: 
  return "Error: No Correct Name"
	  
player_choice_number=name_to_number(choice_name)
print("����ѡ��Ϊ"+choice_name)

comp_number=int(random.randint(0,5) )#�������0,1,2,3,4

def number_to_name(comp_number):#�������������ת��Ϊ����
 if comp_number==0:
   return "ʯͷ"
 elif comp_number==1:
   return "ʷ����"
 elif comp_number==2:
   return "ֽ"
 elif comp_number==3:
   return "����"
 elif comp_number==4:
   return "����"
print("�������ѡ����"+str(number_to_name(comp_number)))

def rpsls(player_choice_number,comp_number):#���ݹ����ж���Ӯ
 if (player_choice_number==comp_number):
    return"���ͼ��������һ����"
 elif (player_choice_number==2 and (comp_number==1 or 0)) or (player_choice_number==3 and (comp_number==1 or 2)):
      return "��Ӯ��!"
 elif (player_choice_number==0 and (comp_number==3 or 4)) or (player_choice_number==1 and (comp_number==4 or 0)) or (player_choice_number==4 and (comp_number==2 or 3)) :  
    return "��Ӯ��!"
 elif (comp_number==2 and (player_choice_number==1 or 0)) or (comp_number==3 and (player_choice_number==1 or 2)):
   return "�����Ӯ��"
 elif (comp_number==0 and (player_choice_number==3 or 4)) or (comp_number==1 and (player_choice_number==4 or 0)) or (comp_number==4 and (player_choice_number==2 or 3)):
	 return "�����Ӯ��"
 else:
	 return "Error: No Correct Name" 

print (rpsls(player_choice_number,comp_number))#������





