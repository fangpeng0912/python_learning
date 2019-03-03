#嵌套

#字典列表
alien_0={'color':'green','points':4}
alien_1={'color':'yellow','points':5}
alien_2={'color':'blue','points':6}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
	
#在字典中存储列表
pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],
	}
#打印所点比萨
print('you have ordered a ' + pizza['crust'] + '-crust pizza with the following toppings:')

for topping in pizza['toppings']:
	print('\t' + topping)
	
#在字典中存储字典
users={
	'fangpeng':{
	'first':'peng',
	'last':'fang',
	'location':'nanjing'
	},
	
	'liwei':{
	'first':'wei',
	'last':'li',
	'location':'shandong',
	},
	
	}
for user_name, user_info in users.items():
	print('\nusername: ' + user_name)
	print('\tFull name: ' + user_info['last'].title() + ' ' + user_info['first'].title())
	print('\tLocation:' + user_info['location'].title())