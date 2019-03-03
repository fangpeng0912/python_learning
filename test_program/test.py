'''
print("hello world")

numbers=[number**2 for number in range(1,5)]
print(numbers)

for i in range(4):
	print(i)
'''

'''	
#if语句，以特殊方式与管理员打招呼
names_list=['admin','zhanglongji','liwei','lihongchao','wangxu']
if names_list == []:
	print("We need to find some users!")
else:
	for name in names_list:
		if name == 'admin':
			print("hello admin, would you like to see the status report?")
		else:
			print("hello eric, thank you for logging in again")
'''

'''
#if语句，检查用户名
current_users=['mengliming','zhanglongji','liwei','lihongchao','wangxu']
new_users=['ZhangLongJi','xiaping','luoshimiao','masenpeng','chenjisihan']
for new_user in new_users:
	used_flag = 0
	for current_user in current_users:
		if new_user.lower() == current_user.lower():
			print(new_user + " has been used, please input other name.")
			used_flag = 1
			break
	if not used_flag:	
		print(new_user + " has not been used")
'''

'''
#if语句，序数	
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(str(number) + 'st')
	elif number == 2:
		print(str(number) + 'nd')
	elif number == 3:
		print(str(number) + 'rd')
	else:
		print(str(number) + 'th')
'''

