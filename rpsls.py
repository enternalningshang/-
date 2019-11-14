#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：向鹏
日期：2019，11，14
"""

import random


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	"""
	将游戏对象对应到不同的整数
	"""
	if name == '石头':
		return 0
	elif name == '史波克':
		return 1
	elif name == '纸':
		return 2
	elif name == '蜥蜴':
		return 3
	elif name == '剪刀':
		return 4
	else:
		return 5#定义函数将输入的对象变为对应的整数，如果没有对应的整数则返回5，后面判断条件要用到


def number_to_name(number):
	"""
	将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	"""
	if number == 0:
		return '石头'
	elif number == 1:
		return '史波克'
	elif number == 2:
		return '纸'
	elif number == 3:
		return '蜥蜴'
	else:
		return '剪刀'#定义函数，将随机产生的数字转换为游戏中的对象


def rpsls(player_choice):
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

	"""
	while player_choice != 'q':
		print('----------------')
		player_choice_number = name_to_number(player_choice)
		comp_number = random.randint(0,4)
		comp_choice = number_to_name(comp_number)
		if player_choice_number == 5:
			print('Error: No Correct Name')#利用name_to_number的返回值判断输入是否在游戏对象中
		else:
			print('您的选择为：%s'%player_choice)
			print('机器的选择为：%s'%comp_choice)
			playerwin = [(0,3),(0,4),(1,0),(1,4),(2,0),(2,1),(3,1),(3,2),(4,2),(4,3)]
			if player_choice_number == comp_number:
				print('您和计算机出的一样呢')#再判断是否相等
			else:
				if (player_choice_number,comp_number) in playerwin:
					print('您赢了')
				else:
					print('计算机赢了')#将player赢的情况输入到一个列表中，如果player与随机产生的数有这里面的关系即在这个列表列表里面，输出您赢了，否则输出计算机赢了
		player_choice = input('继续游戏（输入q退出）:\n')

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择（输入q退出程序）:")
player_choice = input()
rpsls(player_choice)


