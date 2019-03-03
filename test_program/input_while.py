#input函数与while循环
'''
message=input('Tell me something, and i will repeat it back to you:')
print(message)
'''

#删除包含特定值的所有列表元素
#python中in的用法
#1_配合if和while使用,主要返回布尔值true或者false
#if x in X
#if x not in X
#while x in X
#while x not in X
#2_配合for逐个取可迭代对象的元素
#list=[n**2 for n in range(10)]
#for i in list:
#    print(i)

pets=['dog','cat','pig','cat']

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

#使用用户输入来填充字典
favorite_language = {}

input_flag=True

while input_flag:
	name = input("\nwhat's your name? ")
	language = input('which language do you like best? ')
	
	favorite_language[name]=language
	
	repeat = input("Would you like to add another people? (Y/N) ")
	if repeat == 'N' or repeat == 'n':
		input_flag = False
	
print("\nThe result is as follows: ")
for name, language in favorite_language.items():
	print(name + "'s favorite language is " + language)

	