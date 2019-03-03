'''
#字典
favorite_language={
	'chenmeibing':'python',
	'liwei':'java',
	'fangpeng':'c++',
	'lihongchao':'python'
	}

#遍历键值，用keys()方法或者默认，遍历值用values()方法，遍历字典用items()方法，sorted函数临时排序
for name,language in sorted(favorite_language.items()):
	print("\nname: " + name.title())
	print("favorite language: " + language.title())
	
#使用set集合避免重复
for language in set(favorite_language.values()):
	print("\n" + language.title())
'''


