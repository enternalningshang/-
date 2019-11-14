#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2019��11��14
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name == 'ʯͷ':
		return 0
	elif name == 'ʷ����':
		return 1
	elif name == 'ֽ':
		return 2
	elif name == '����':
		return 3
	elif name == '����':
		return 4
	else:
		return 5#���庯��������Ķ����Ϊ��Ӧ�����������û�ж�Ӧ�������򷵻�5�������ж�����Ҫ�õ�


def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number == 0:
		return 'ʯͷ'
	elif number == 1:
		return 'ʷ����'
	elif number == 2:
		return 'ֽ'
	elif number == 3:
		return '����'
	else:
		return '����'#���庯�������������������ת��Ϊ��Ϸ�еĶ���


def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

	"""
	while player_choice != 'q':
		print('----------------')
		player_choice_number = name_to_number(player_choice)
		comp_number = random.randint(0,4)
		comp_choice = number_to_name(comp_number)
		if player_choice_number == 5:
			print('Error: No Correct Name')#����name_to_number�ķ���ֵ�ж������Ƿ�����Ϸ������
		else:
			print('����ѡ��Ϊ��%s'%player_choice)
			print('������ѡ��Ϊ��%s'%comp_choice)
			playerwin = [(0,3),(0,4),(1,0),(1,4),(2,0),(2,1),(3,1),(3,2),(4,2),(4,3)]
			if player_choice_number == comp_number:
				print('���ͼ��������һ����')#���ж��Ƿ����
			else:
				if (player_choice_number,comp_number) in playerwin:
					print('��Ӯ��')
				else:
					print('�����Ӯ��')#��playerӮ��������뵽һ���б��У����player���������������������Ĺ�ϵ��������б��б����棬�����Ӯ�ˣ�������������Ӯ��
		player_choice = input('������Ϸ������q�˳���:\n')

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ������q�˳�����:")
player_choice = input()
rpsls(player_choice)


